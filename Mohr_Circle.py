import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.widgets import TextBox

# Function to update the Mohr Circle plot when input values change
def update_plot(val):
    # Clear the current plot and set grid and title
    ax.clear()
    ax.grid(True)
    ax.set_title('Mohr Circle')
    
    # Get current input values of σ_x, σ_y, and τ_xy from text boxes
    s_x = float(text_box_1.text)
    s_y = float(text_box_2.text)
    t_xy = float(text_box_3.text)
    
    # Calculate center and radius of the Mohr Circle
    center = (s_x + s_y) / 2
    radius = np.sqrt(((s_x - s_y) / 2) ** 2 + t_xy ** 2)

    # Draw the Mohr Circle
    circle = plt.Circle((center, 0), radius, facecolor='cyan', edgecolor='black', fill=True, alpha=1)
    ax.add_artist(circle)

    # Compute principal angle θ_p and shear angle θ_s (halved for Mohr Circle)
    theta_p = np.arctan(2 * t_xy / (s_x - s_y)) / 2
    theta_s = np.pi / 2 - theta_p

    # Convert angles to degrees
    rotated_angle_deg_p = theta_p * 180 / np.pi
    rotated_angle_deg_s = theta_s * 180 / np.pi

    # Calculate coordinates for plotting principal and shear stress lines
    x_input = [
        center - radius * np.cos(theta_p),
        center,
        center + radius * np.cos(theta_p),
        center - radius * np.cos(theta_s),
        center + radius * np.cos(theta_s)
    ]
    y_input = [
        -radius * np.sin(theta_p),
        0,
        radius * np.sin(theta_p),
        -radius * np.sin(theta_s),
        radius * np.sin(theta_s)
    ]

    # Plot stress lines on the Mohr Circle
    ax.plot([x_input[0], x_input[2]], [y_input[0], y_input[2]], linestyle='--', color='red')
    ax.plot([x_input[3], x_input[4]], [y_input[3], y_input[4]], linestyle='--', color='red')
    ax.plot([center - radius, center + radius], [0, 0], linestyle='--', color='black')
    ax.plot([center, center], [-radius, radius], linestyle='--', color='black')

    # Plot the principal angle θ_p and add an arc for visualization
    ax.annotate('', xy=(center + 0.40 * radius * np.cos(theta_p), 0.40 * radius * np.sin(theta_p)), xytext=(center, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(center + 0.40 * radius * np.cos(theta_p), 0.40 * radius * np.sin(theta_p) - 0.1 * radius, 
            r'$\theta_p$' + f' = {rotated_angle_deg_p:.1f}' + r'$^\circ$', fontsize=14)
    arc_p = Arc((center, 0), 0.5 * radius, 0.5 * radius, angle=0, theta1=0, theta2=rotated_angle_deg_p, 
                edgecolor='black', linestyle='dashed', linewidth=1.5)
    ax.add_patch(arc_p)

    # Plot the shear angle θ_s and add an arc for visualization
    ax.annotate('', xy=(center + 0.40 * radius * np.cos(theta_s), 0.40 * radius * np.sin(theta_s)), xytext=(center, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(center + 0.40 * radius * np.cos(theta_s), 0.40 * radius * np.sin(theta_s) - 0.1 * radius, 
            r'$\theta_s$' + f' = {rotated_angle_deg_s:.1f}' + r'$^\circ$', fontsize=14)
    arc_s = Arc((center, 0), 0.5 * radius, 0.5 * radius, angle=0, theta1=rotated_angle_deg_s, theta2=0, 
                edgecolor='black', linestyle='dashed', linewidth=1.5)
    ax.add_patch(arc_s)

    # Set the limits of the plot based on the circle dimensions
    ax.set_xlim([center - radius - 5, center + radius + 5])
    ax.set_ylim([-radius - 5, radius + 5])

    # Plot points for σ_avg, σ_max, σ_min, τ_max, and τ_min
    x_pt = [center, center + radius, center - radius, center, center]
    y_pt = [0, 0, 0, radius, -radius]
    labels = [r'$\sigma_{avg}$', r'$\sigma_{max}$', r'$\sigma_{min}$', r'$\tau_{max}$', r'$\tau_{min}$']
    for x, y, label in zip(x_pt, y_pt, labels):
        ax.text(x + 0.5, y, label, fontsize=14)
        ax.scatter(x, y, color='red')

    # Final adjustments and plot redraw
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)
    plt.draw()

# Initialize the plot and set up the figure
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.2)

# Initial values for stresses σ_x, σ_y, and τ_xy
s1 = 20
s2 = 10
t1 = 5

# Draw the initial Mohr Circle with these values
center_i = (s1 + s2) / 2
rad_i = np.sqrt(((s1 - s2) ** 2) / 4 + t1 ** 2)
initial_circle = plt.Circle((center_i, 0), rad_i, fill=False)
ax.add_artist(initial_circle)

# Set plot limits and grid for the initial plot
ax.set_xlim([center_i - rad_i - 10, center_i + rad_i + 10])
ax.set_ylim([-rad_i - 10, rad_i + 10])
ax.grid(True)

# Add input text boxes for σ_x, σ_y, and τ_xy
axbox_1 = plt.axes([0.15, 0.05, 0.08, 0.075])
text_box_1 = TextBox(axbox_1, r'$\sigma_x$ ', initial=str(s1))
text_box_1.label.set_fontsize(12)

axbox_2 = plt.axes([0.4, 0.05, 0.1, 0.075])
text_box_2 = TextBox(axbox_2, r'$\sigma_y$ ', initial=str(s2))
text_box_2.label.set_fontsize(12)

axbox_3 = plt.axes([0.65, 0.05, 0.1, 0.075])
text_box_3 = TextBox(axbox_3, r'$\tau_{xy}$', initial=str(t1))
text_box_3.label.set_fontsize(12)

# Bind the text boxes to the update function
text_box_1.on_submit(update_plot)
text_box_2.on_submit(update_plot)
text_box_3.on_submit(update_plot)

# Show the initial plot
plt.show()
