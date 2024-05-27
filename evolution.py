import numpy as np
import scipy.ndimage as ndimage

STAR_PATTERN = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
])

def can_form_star(universe, i, j):
    rows, cols = universe.shape
    pattern_rows, pattern_cols = STAR_PATTERN.shape

    if i > rows - pattern_rows or j > cols - pattern_cols:
        return False

    for m in range(pattern_rows):
        for n in range(pattern_cols):
            if STAR_PATTERN[m, n] == 1 and universe[i + m, j + n] != 0:
                return False

    return True

def form_star(universe, i, j):
    pattern_rows, pattern_cols = STAR_PATTERN.shape

    for m in range(pattern_rows):
        for n in range(pattern_cols):
            if STAR_PATTERN[m, n] == 1:
                universe[i + m, j + n] = 3

def calculate_potential(universe):
    mass_distribution = (universe == 1) + (universe == 2) + 2 * (universe == 3) + 3 * (universe == 4)
    potential = ndimage.gaussian_filter(mass_distribution.astype(float), sigma=3)
    return potential

def drift_matter(universe, potential):
    new_universe = np.copy(universe)
    rows, cols = universe.shape

    for i in range(rows):
        for j in range(cols):
            if universe[i, j] in [1, 2]:
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                best_neighbor = max(neighbors, key=lambda pos: potential[pos] if 0 <= pos[0] < rows and 0 <= pos[1] < cols else -np.inf)
                
                if potential[best_neighbor] > potential[i, j]:
                    new_universe[best_neighbor] = universe[i, j]
                    new_universe[i, j] = 0

    return new_universe

def check_star_size(universe, i, j):
    star_cluster = np.sum(universe[max(0, i-1):min(i+2, universe.shape[0]), max(0, j-1):min(j+2, universe.shape[1])] == 3)
    if star_cluster >= 9:  # Threshold for supernova
        universe[max(0, i-1):min(i+2, universe.shape[0]), max(0, j-1):min(j+2, universe.shape[1])] = 4

def evolve_universe(universe):
    new_universe = np.copy(universe)
    rows, cols = universe.shape
    potential = calculate_potential(universe)

    for i in range(rows):
        for j in range(cols):
            hydrogen_neighbors = np.sum(universe[max(0, i-1):min(i+2, rows), max(0, j-1):min(j+2, cols)] == 1)
            helium_neighbors = np.sum(universe[max(0, i-1):min(i+2, rows), max(0, j-1):min(j+2, cols)] == 2)

            if universe[i, j] == 0:
                if hydrogen_neighbors > 1 and np.random.rand() < 0.1:
                    new_universe[i, j] = 1
                elif helium_neighbors > 1 and np.random.rand() < 0.1:
                    new_universe[i, j] = 2
            elif universe[i, j] == 1 or universe[i, j] == 2:
                if hydrogen_neighbors > 0 and helium_neighbors > 0 and np.random.rand() < 0.05:
                    if can_form_star(new_universe, i, j):
                        form_star(new_universe, i, j)
            elif universe[i, j] == 3:
                if np.random.rand() < 0.01:
                    new_universe[i, j] = 0

    new_universe = drift_matter(new_universe, potential)
    return new_universe
