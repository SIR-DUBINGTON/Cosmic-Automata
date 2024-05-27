import numpy as np

def initialize_universe(size, num_states=5):
    """
    Initializes the universe with random states.
    States: 0 = empty space, 1 = hydrogen, 2 = helium, 3 = star, 4 = black hole
    """
    return np.random.choice(range(num_states - 2), size=size)  # Avoid initializing with black holes and stars
