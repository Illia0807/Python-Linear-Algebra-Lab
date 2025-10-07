import numpy as np
import matplotlib.pyplot as plt

def get_vector_from_user(prompt):
    """
    Asks the user for a 3D vector and returns it as a NumPy array.
    Handles input errors.
    """
    while True:
        try:
            user_input = input(prompt)
            # Split the input by commas and convert to float numbers
            components = [float(comp) for comp in user_input.split(',')]
            if len(components) != 3:
                raise ValueError("Vector must have 3 components.")
            # Convert the list to a NumPy array
            return np.array(components)
        except ValueError as e:
            print(f"Error: {e}. Please enter 3 numbers separated by commas (e.g., 1,1,0).")

# --- 1. Get user input ---
print("--- Defining the Plane ---")
print("Enter the two base vectors that form the plane.")
v = get_vector_from_user("Enter components for vector v (e.g., 1,1,0): ")
w = get_vector_from_user("Enter components for vector w (e.g., 0,1,1): ")

print("\n--- Checking a Vector ---")
u = get_vector_from_user("Enter components for vector u to check (e.g., 1,2,3): ")

# --- 2. The Algebra: Calculations ---

# Find the normal vector (perpendicular) to the plane via the cross product
normal_vector = np.cross(v, w)

# Check if the vectors are parallel (in which case they don't form a plane)
if np.all(normal_vector == 0):
    print("\nError: Vectors v and w are parallel and cannot form a plane.")
else:
    # Check if vector u lies on the plane.
    # This is true if u is perpendicular to the normal vector.
    # We check this using the dot product. If it's zero, the vectors are perpendicular.
    dot_product = np.dot(normal_vector, u)

    # --- 3. The Geometry: Visualization ---
    
    # Create the 3D plot
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # --- Draw the base vectors v and w ---
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='red', arrow_length_ratio=0.1, label=f'Vector v = {v}')
    ax.quiver(0, 0, 0, w[0], w[1], w[2], color='blue', arrow_length_ratio=0.1, label=f'Vector w = {w}')

    # --- Draw the vector u to be checked ---
    # np.isclose is used to compare floating-point numbers instead of '=='
    if np.isclose(dot_product, 0):
        result_text = f"Vector u = {u} IS on the plane."
        u_color = 'green'
    else:
        result_text = f"Vector u = {u} is NOT on the plane."
        u_color = 'purple'
    
    print(f"\nCheck Result: {result_text}")
    ax.quiver(0, 0, 0, u[0], u[1], u[2], color=u_color, arrow_length_ratio=0.1, label=result_text)

    # --- Draw the plane ---
    # Create a grid for the plane surface
    # Find the maximum range for a nice plot display
    max_range = np.max(np.abs(np.concatenate((v, w, u)))) * 1.5
    
    xx, yy = np.meshgrid(np.linspace(-max_range, max_range, 10),
                         np.linspace(-max_range, max_range, 10))

    # Calculate z using the plane equation: ax + by + cz = 0  => z = (-ax - by) / c
    a, b, c = normal_vector
    if c != 0: # Avoid division by zero if the plane is vertical to the Z-axis
        zz = (-a * xx - b * yy) / c
        ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan', rstride=100, cstride=100)

    # --- Plot final setup and display ---
    ax.set_xlabel('X-Axis', fontsize=12)
    ax.set_ylabel('Y-Axis', fontsize=12)
    ax.set_zlabel('Z-Axis', fontsize=12)
    
    plane_eq = f"{a:.2f}x + {b:.2f}y + {c:.2f}z = 0"
    ax.set_title(f"Vector Visualization\nPlane Equation: {plane_eq}", fontsize=14)
    
    ax.legend(fontsize=10)
    ax.view_init(elev=20, azim=30) # Set the viewing angle
    
    # Set equal aspect ratio for all axes
    ax.set_box_aspect([1,1,1])

    plt.show()