import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

def animate_universe(universe, evolve_universe, expand_universe, expansion_rate, num_steps=100):
    """
    Animates the evolution of the universe.
    """
    fig, ax = plt.subplots()

    # Define a custom colormap with a brighter red for black holes
    cmap = mcolors.ListedColormap(['black', 'white', 'blue', 'yellow', '#FF4500'])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    im = ax.imshow(universe, cmap=cmap, norm=norm, animated=True)

    def update(frame):
        nonlocal universe
        if frame % 1000 == 0:  # Expand the universe every 10 frames
            universe = expand_universe(universe, expansion_rate)
        universe = evolve_universe(universe)
        im.set_array(universe)
        ax.set_title(f"Step {frame}")

        if frame == num_steps - 1:
            print("Simulation has reached its final step.")
            ax.text(0.5, 1.05, "Simulation Complete", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=12, color='red')

        return im,

    ani = animation.FuncAnimation(fig, update, frames=num_steps, blit=True, repeat=False)
    plt.show()
