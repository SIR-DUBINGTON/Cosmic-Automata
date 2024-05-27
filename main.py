from universe import initialize_universe
from evolution import evolve_universe,np
from visualization import animate_universe

def expand_universe(universe, expansion_rate):
    """
    Expands the universe grid by adding empty cells around the edges.
    """
    rows, cols = universe.shape
    new_rows = int(rows * expansion_rate)
    new_cols = int(cols * expansion_rate)
    new_universe = np.zeros((new_rows, new_cols), dtype=int)
    new_universe[:rows, :cols] = universe
    return new_universe

def main():
    # Define the initial size of the universe (grid)
    universe_size = (100, 100)
    expansion_rate = 1.1  # Define how much the universe expands each step

    # Initialize the universe with random states (0 for empty space, 1 for hydrogen, 2 for helium)
    universe = initialize_universe(universe_size, num_states=5)

    # Number of steps for the simulation
    num_steps = 200

    # Run the animation
    animate_universe(universe, evolve_universe, expand_universe, expansion_rate, num_steps)

if __name__ == "__main__":
    main()
