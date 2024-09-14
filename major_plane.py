import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import TextBox
import numpy as np

# Initialize figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot when values change
def update(val):
    # Clear the current plot
    ax.clear()

    # Define the vertices of a cube
    cube_vertices = np.array([
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ])

    # Define the faces of the cube using the vertices
    faces = [
        [cube_vertices[j] for j in [0, 1, 2, 3]],  # Bottom face
        [cube_vertices[j] for j in [4, 5, 6, 7]],  # Top face
        [cube_vertices[j] for j in [0, 1, 5, 4]],  # Front face
        [cube_vertices[j] for j in [2, 3, 7, 6]],  # Back face
        [cube_vertices[j] for j in [1, 2, 6, 5]],  # Right face
        [cube_vertices[j] for j in [0, 3, 7, 4]]   # Left face
    ]

    # Plot the cube with a light color and red edges
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.25))

    # Set plot limits and labels
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.view_init(elev=20., azim=135)  # Set initial view angle

    # Get input values for σ_x, σ_y, and τ_xy
    sigma_x = float(text_box_5.text)
    sigma_y = float(text_box_6.text)
    tau_xy = float(text_box_7.text)

    # Calculate the rotation angle (Mohr Circle approximation)
    rotation_angle = np.arctan(np.divide(2 * tau_xy, (sigma_x - sigma_y))) / 2

    # Define the normal vector for the rotated plane
    theta = rotation_angle
    normal = np.array([-np.sin(theta), np.cos(theta), 1])

    # Get input for the point coordinates (X, Y, Z)
    input_point = (float(text_box_1.text), float(text_box_2.text), float(text_box_3.text))

    # Create meshgrid for the plane
    xx, yy = np.meshgrid(np.linspace(0, 1, 10), np.linspace(0, 1, 10))

    # Define the plane equation and calculate z-coordinates for the plane
    d = normal[0] * input_point[0] + normal[1] * input_point[1] + normal[2] * input_point[2]
    zz = (-normal[0] * xx - normal[1] * yy + d) / normal[2]

    # Plot the rotated plane with a semi-transparent green color
    ax.plot_surface(xx, yy, zz, color='green', alpha=0.5)

    # Plot the input point on the 3D plot
    ax.scatter3D(input_point[0], input_point[1], input_point[2], color='red', s=100, zorder=4, alpha=1)
    ax.text3D(input_point[0] + 0.05, input_point[1] + 0.05, input_point[2] + 0.05, 'Point', fontsize=14)

    # Redraw the updated plot
    plt.draw()

# Define the vertices of a cube
cube_vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
])

# Define the faces of the cube
faces = [
    [cube_vertices[j] for j in [0, 1, 2, 3]],  # Bottom face
    [cube_vertices[j] for j in [4, 5, 6, 7]],  # Top face
    [cube_vertices[j] for j in [0, 1, 5, 4]],  # Front face
    [cube_vertices[j] for j in [2, 3, 7, 6]],  # Back face
    [cube_vertices[j] for j in [1, 2, 6, 5]],  # Right face
    [cube_vertices[j] for j in [0, 3, 7, 4]]   # Left face
]

# Plot the initial cube
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.25))

# Set the initial plot limits and labels
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.view_init(elev=20., azim=135)

# Create text boxes for input (X, Y, Z coordinates)
axbox_1 = plt.axes([0.15, 0.05, 0.08, 0.075])
text_box_1 = TextBox(axbox_1, r'$X$', initial=str(0.5))

axbox_2 = plt.axes([0.4, 0.05, 0.1, 0.075])
text_box_2 = TextBox(axbox_2, r'$Y$', initial=str(0.5))

axbox_3 = plt.axes([0.65, 0.05, 0.1, 0.075])
text_box_3 = TextBox(axbox_3, r'$Z$', initial=str(0.5))

# Create text boxes for σ_x, σ_y, and τ_xy values
axbox_5 = plt.axes([0.15, 0.9, 0.1, 0.075])
text_box_5 = TextBox(axbox_5, r'$\sigma_x$', initial=str(30))

axbox_6 = plt.axes([0.4, 0.9, 0.1, 0.075])
text_box_6 = TextBox(axbox_6, r'$\sigma_y$', initial=str(0.5))

axbox_7 = plt.axes([0.65, 0.9, 0.1, 0.075])
text_box_7 = TextBox(axbox_7, r'$\tau_{xy}$', initial=str(0.5))

# Bind the text box inputs to the update function
text_box_3.on_submit(update)

# Display the plot
plt.show()
