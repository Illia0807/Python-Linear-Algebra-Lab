import numpy as np
import matplotlib.pyplot as plt

# --- 1. Setup ---
# Define our two base vectors. You can change these to experiment.
v = np.array([4, 1])
w = np.array([1, 3])

# Create the figure and axes for plotting
fig, ax = plt.subplots(figsize=(8, 8))

# --- Function to draw the background (vectors, diagonals) ---
def draw_background():
    ax.clear() # Clear previous points from the plot
    # Draw the base vectors v and w
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'v = {v}')
    ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'w = {w}')
    
    # Draw the other two sides of the parallelogram
    ax.plot([v[0], v[0]+w[0]], [v[1], v[1]+w[1]], 'b--')
    ax.plot([w[0], v[0]+w[0]], [w[1], v[1]+w[1]], 'r--')

    # Draw the diagonals
    # Main diagonal (v+w)
    ax.plot([0, v[0]+w[0]], [0, v[1]+w[1]], 'g:', label='Main Diagonal (c=d)')
    # Second diagonal (v-w)
    ax.plot([w[0], v[0]], [w[1], v[1]], 'm:', label='Second Diagonal (c+d=1)')
    
    # Plot settings
    ax.grid(True)
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_title("Linear Combination Lab")
    ax.legend()
    # Set equal aspect ratio for the axes
    ax.set_aspect('equal', adjustable='box')
    # Set axis limits to ensure everything is visible
    max_val = max(abs(v[0]+w[0]), abs(v[1]+w[1])) + 2
    ax.axis([-max_val, max_val, -max_val, max_val])

# --- 2. Main Loop ---
while True:
    draw_background() # Draw the background vectors and lines
    
    try:
        c_input = input("Enter coefficient 'c' (or 'exit' to quit): ")
        if c_input.lower() == 'exit':
            break
        c = float(c_input)
        
        d_input = input("Enter coefficient 'd': ")
        if d_input.lower() == 'exit':
            break
        d = float(d_input)

        # Calculate the linear combination
        point = c * v + d * w
        
        # --- 3. Analysis and Magic ---
        analysis = ""
        # Check the rules. np.isclose is used to compare floating-point numbers.
        if np.isclose(c, d):
            analysis = "Rule: c = d. The point lies on the main diagonal."
        elif np.isclose(c + d, 1):
            analysis = "Rule: c + d = 1. The point lies on the line connecting the vector tips."
        else:
            analysis = "This is a general linear combination."

        print(f"\nResult: c*v + d*w = {point}")
        print(f"Analysis: {analysis}\n")
        
        # --- 4. Visualization ---
        # Plot the resulting point
        ax.plot(point[0], point[1], 'ko', markersize=10, label=f'Point p = ({point[0]:.2f}, {point[1]:.2f})')
        ax.legend()
        plt.show()

    except ValueError:
        print("Error: Please enter numbers.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

print("Program finished.")