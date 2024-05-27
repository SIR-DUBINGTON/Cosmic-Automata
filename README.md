# Cosmic Automata

Cosmic Automata is a fascinating simulation project that explores the formation and evolution of a universe using cellular automata principles. Inspired by Stephen Wolfram's ideas, this project models complex interactions such as the formation of stars and black holes within an expanding grid of cells.

Features

    Cellular Automata Simulation: Utilizes cellular automata to model the dynamic behavior of the universe.
    Specific Star Patterns: Implements a predefined 5x5 pattern for star formation, ensuring stars maintain a specific shape.
    Matter Evolution: Simulates hydrogen and helium interactions leading to star formation and potential supernovae, resulting in black holes.
    Dynamic Expansion: Includes grid expansion over time to mimic the expanding nature of the universe.
    Visual Representation: Uses Matplotlib for live updating visualizations, with distinct colors for different states (empty space, hydrogen, helium, stars, black holes).

Installation

Clone the Repository:

git clone <repository-url>

cd cosmic_automata

Install Dependencies:

Ensure you have Python installed. Install the required libraries using pip:

pip install numpy scipy matplotlib

How to Run

Navigate to the project directory:

cd cosmic_automata (for example)

Run the simulation:

    python main.py

Project Structure

    main.py: Entry point for running the simulation. Initializes the universe and handles expansion.
    universe.py: Handles the initialization of the universe grid.
    evolution.py: Defines the rules for the evolution of the universe, including star formation and growth, as well as black hole creation.
    visualization.py: Manages the live updating visualization using Matplotlib.

How It Works
Initialization

The universe is represented as a grid where each cell can be in one of several states:

    0: Empty space (Black)
    1: Hydrogen (White)
    2: Helium (Blue)
    3: Star (Yellow)
    4: Black Hole (Brighter Red)

Evolution

    Matter Interaction: Hydrogen and helium can collide to form stars, which follow a specific 5x5 pattern.
    Star Growth and Supernova: Stars grow by absorbing more hydrogen and helium. When they reach a certain size, they undergo a supernova, turning into black holes.
    Matter Drift: Matter moves towards areas with higher mass concentration, simulating gravitational effects.

Visualization

The simulation uses Matplotlib to provide a live updating visualization, displaying the evolution of the universe over time. Different colors are used to represent different states of matter.

Contributions

Contributions are welcome! If you have ideas for improvements, new features or a deeper understanding of physics and feel I need to alter anything currently in the simulation, 
please feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any questions or suggestions, please reach out via GitHub issues.
