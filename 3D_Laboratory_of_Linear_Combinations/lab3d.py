import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# --- 1. Turn on interactive mode ---
plt.ion()

# --- 2. Scene Setup ---
# Define three base vectors. These vectors create a large triangle.
u = np.array([10, 0, 0])
v = np.array([0, 10, 0])
w = np.array([0, 0, 10])

# Create the 3D plot ONCE
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# --- 3. Draw the static background ONCE ---
# Large gold marker at the origin
ax.scatter(0, 0, 0, color='gold', s=150, edgecolor='black', label='Origin (0,0,0)', zorder=10)
# Base vectors
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='r', label=f'u = {u}')
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='g', label=f'v = {v}')
ax.quiver(0, 0, 0, w[0], w[1], w[2], color='b', label=f'w = {w}')
# Dashed triangle
verts = [list(u), list(v), list(w)]
triangle = Poly3DCollection([verts], alpha=0.2, facecolor='cyan')
ax.add_collection3d(triangle)
ax.plot([u[0], v[0]], [u[1], v[1]], [u[2], v[2]], 'k--')
ax.plot([v[0], w[0]], [v[1], w[1]], [v[2], w[2]], 'k--')
ax.plot([w[0], u[0]], [w[1], u[1]], [w[2], u[2]], 'k--')
# Scene settings
ax.set_xlabel('X-Axis'); ax.set_ylabel('Y-Axis'); ax.set_zlabel('Z-Axis')
ax.set_title('Interactive 3D Lab')
max_val = np.max(np.abs(np.vstack([u, v, w]))) + 2
ax.set_xlim([0, max_val]); ax.set_ylim([0, max_val]); ax.set_zlim([0, max_val])
ax.legend()

# Variables to store the plots we need to update
current_point_plot = None
current_line_plot = None

# --- 4. Main loop for updates ---
while True:
    try:
        # Get input from the terminal
        prompt = "Enter c, d, e separated by spaces (e.g., '0.5 0.5 0') or 'exit' to quit: "
        user_input = input(prompt)

        if user_input.lower() == 'exit':
            break

        # Parse the input
        c, d, e = map(float, user_input.split())
        
        # Calculate the new point
        point = c*u + d*v + e*w
        
        # --- Remove the old point and line from the plot ---
        if current_point_plot:
            current_point_plot.remove()
        if current_line_plot:
            # The comma is needed because ax.plot returns a list of lines
            current_line_plot.remove()

        # --- Analysis ---
        # (The analysis logic remains the same)
        analysis = []
        if np.isclose(c + d + e, 1):
            analysis.append("Rule: c+d+e = 1. The point lies on the plane of the triangle.")
            if c >= 0 and d >= 0 and e >= 0:
                analysis.append("-> Since c,d,e >= 0, the point is INSIDE the triangle.")
        else:
             analysis.append("This is a general linear combination in 3D space.")
        
        print("\n" + "\n".join(analysis) + "\n")
        
        # --- Draw the new point ---
        label = f'Point p = ({point[0]:.1f}, {point[1]:.1f}, {point[2]:.1f})'
        current_point_plot = ax.scatter(point[0], point[1], point[2], color='black', s=150, edgecolor='white', label=label, zorder=5)
        
        # --- NEW: Draw a dashed line to the point ---
        current_line_plot, = ax.plot([0, point[0]], [0, point[1]], [0, point[2]], 'k--', zorder=5)

        # Update the legend and the plot window
        ax.legend()
        fig.canvas.draw()
        fig.canvas.flush_events()

    except (ValueError, IndexError):
        print("Error: Please enter three numbers separated by spaces, or 'exit'.\n")

# --- 5. Clean Up ---
plt.ioff() # Turn off interactive mode
plt.close(fig) # Close the plot window
print("Program finished.")