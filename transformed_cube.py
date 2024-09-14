import matplotlib.pyplot as plt
from math import cos, sin, sqrt, atan2, pi
from matplotlib.patches import Arc


fig, ax=plt.subplots(figsize=(9,9))

def stress_transformation(sigma_x, sigma_y, tau_xy, theta):

    # Calculate transformed stresses
    sigma_x_prime = sigma_x * cos(theta)**2 + sigma_y * sin(theta)**2 + 2 * tau_xy * sin(theta) * cos(theta)
    sigma_y_prime = sigma_x * sin(theta)**2 + sigma_y * cos(theta)**2 - 2 * tau_xy * sin(theta) * cos(theta)
    tau_xy_prime = (sigma_y - sigma_x) * sin(2 * theta) / 2 + tau_xy * cos(2 * theta)

    # Calculate maximum stresses
    max_sigma_1 = (sigma_x_prime + sigma_y_prime) / 2 + sqrt(((sigma_x_prime - sigma_y_prime) / 2)**2 + tau_xy_prime**2)
    max_sigma_2 = (sigma_x_prime + sigma_y_prime) / 2 - sqrt(((sigma_x_prime - sigma_y_prime) / 2)**2 + tau_xy_prime**2)

    # Calculate maximum shear stress
    max_tau = abs(tau_xy_prime)

    return sigma_x_prime, sigma_y_prime, tau_xy_prime

def plot_rotated_cube(val):

    ax.clear()

    sigma_x=float(text_box_1.text)
    sigma_y=float(text_box_2.text)
    tau_xy=float(text_box_3.text)
    theta=float(text_box_4.text)*np.pi/180

    # plt.clear()
    # Calculate maximum stresses and strains
    new_sigma_x, new_sigma_y, new_tau_xy = stress_transformation(sigma_x, sigma_y, tau_xy, theta)

    # Draw the rotated 2D cube on coordinate axes
    # plt.figure(figsize=(8, 8))

    # Rotated cube
    rotated_x_1 = 0
    rotated_y_1 = 0
    rotated_x_2 = cos(theta)
    rotated_y_2 = sin(theta)
    rotated_x_3 = np.sqrt(2)*cos(theta + np.pi/4)
    rotated_y_3 = np.sqrt(2)*sin(theta+np.pi/4)
    rotated_x_4 = -sin(theta)
    rotated_y_4 = cos(theta)
    # plt.scatter(rotated_x_2,rotated_y_2)
    ax.plot([rotated_x_1, rotated_x_2, rotated_x_3, rotated_x_4, rotated_x_1], 
             [rotated_y_1, rotated_y_2, rotated_y_3, rotated_y_4, rotated_y_1], 'black', label='Rotated cube')


    square_x = [rotated_x_1, rotated_x_2, rotated_x_3, rotated_x_4]
    square_y = [rotated_y_1, rotated_y_2, rotated_y_3, rotated_y_4]

    # Add face color to the square
    ax.fill(square_x, square_y, 'cyan', alpha=0.5)
    # Add an arrowhead to the arc
    ax.annotate('', xy=(0.25*cos(theta), 0.25*sin(theta)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5))

    # Display the rotation angle in degrees
    rotated_angle_deg = (theta * 180 / pi) % 360  # Adjusting the angle to be within 0-360 degrees


    
    arc = Arc((0, 0), 0.5, 0.5, angle=0, theta1=0, theta2=rotated_angle_deg, edgecolor='black', linestyle='dashed', linewidth=1.5)
    ax.add_patch(arc)


    ax.annotate('', xy=((rotated_x_2+rotated_x_3)/2 + 0.25*cos(theta),(rotated_y_2+rotated_y_3)/2+0.25*sin(theta)), xytext=((rotated_x_2+rotated_x_3)/2, (rotated_y_2+rotated_y_3)/2),
                 arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text((rotated_x_2+rotated_x_3)/2 + 0.25,(rotated_y_2+rotated_y_3)/2+0.25, r'$\sigma_{x}$' + f'={new_sigma_x:.2f}', fontsize=14)


    ax.annotate('', xy=((rotated_x_3+rotated_x_4)/2 - 0.25*sin(theta),(rotated_y_3+rotated_y_4)/2+0.25*cos(theta)), xytext=((rotated_x_4+rotated_x_3)/2, (rotated_y_4+rotated_y_3)/2),
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text((rotated_x_4+rotated_x_3)/2 - 0.30,(rotated_y_4+rotated_y_3)/2+0.25, r'$\sigma_{y}$'+f'={new_sigma_y:.2f}', fontsize=14)


    ax.annotate('', xy=((rotated_x_4+rotated_x_1)/2 - 0.25*cos(theta),(rotated_y_4+rotated_y_1)/2-0.25*sin(theta)), xytext=((rotated_x_4+rotated_x_1)/2, (rotated_y_4+rotated_y_1)/2),
                 arrowprops=dict(arrowstyle="->", lw=1.5))
    
    ax.annotate('', xy=((rotated_x_2+rotated_x_1)/2 + 0.25*sin(theta),(rotated_y_2+rotated_y_1)/2-0.25*cos(theta)), xytext=((rotated_x_2+rotated_x_1)/2, (rotated_y_2+rotated_y_1)/2),
                arrowprops=dict(arrowstyle="->", lw=1.5))
    

    ax.annotate('', xy=(rotated_x_1,rotated_y_1-0.05), xytext=(rotated_x_2, rotated_y_2-0.05),
            arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(rotated_x_3,rotated_y_3+0.05, r'$\tau_{xy}$'+f'={new_tau_xy:.2f}', fontsize=14)
    
    ax.annotate('', xy=(rotated_x_3,rotated_y_3+0.05), xytext=(rotated_x_2, rotated_y_2+0.05),
        arrowprops=dict(arrowstyle="->", lw=1.5))
    
    ax.annotate('', xytext=(rotated_x_4-0.05,rotated_y_4+0.05), xy=(rotated_x_3-0.05, rotated_y_3+0.05),
        arrowprops=dict(arrowstyle="->", lw=1.5))
    
    ax.annotate('', xy=(rotated_x_1-0.05,rotated_y_1), xytext=(rotated_x_4-0.05, rotated_y_4),
    arrowprops=dict(arrowstyle="->", lw=1.5))

    # Add an arrowhead to the arc
    ax.annotate('', xy=(0.25*cos(theta), 0.25*sin(theta)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate('', xy=(0.25,0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5))
    # plt.text(0, -0.2, f'Rotated Angle: {rotated_angle_deg:.2f} degrees', fontsize=12, ha='center')
    ax.text(0.3,0.1,f'{rotated_angle_deg:.2f}'+r'$^\circ$', fontsize=12, ha='center')

    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Rotated 2D Cube by {rotated_angle_deg:.1f}'+r'$^\circ$', fontsize=18)
    # ax.legend()

    # plt.tight_layout()
    # ax.set_autoscale_on()
    # ax.set_xlim([-2,1.41])
    # ax.set_ylim([-0.2,1.5])
    # plt.axis('equal')
    ax.margins(0.2)
    plt.draw()


ax.set_title('Static 2D Cube', fontsize=18)

theta=0
rotated_x_1 = 0
rotated_y_1 = 0
rotated_x_2 = cos(theta)
rotated_y_2 = sin(theta)
rotated_x_3 = np.sqrt(2)*cos(theta + np.pi/4)
rotated_y_3 = np.sqrt(2)*sin(theta+np.pi/4)
rotated_x_4 = -sin(theta)
rotated_y_4 = cos(theta)
# plt.tight_layout()
# plt.scatter(rotated_x_2,rotated_y_2)
ax.plot([rotated_x_1, rotated_x_2, rotated_x_3, rotated_x_4, rotated_x_1], 
            [rotated_y_1, rotated_y_2, rotated_y_3, rotated_y_4, rotated_y_1], 'black', label='Rotated cube')

square_x = [rotated_x_1, rotated_x_2, rotated_x_3, rotated_x_4]
square_y = [rotated_y_1, rotated_y_2, rotated_y_3, rotated_y_4]

# Add face color to the square
ax.fill(square_x, square_y, 'cyan', alpha=0.5)

ax.margins(0.2)

axbox_1 = plt.axes([0.15, 0.01, 0.075, 0.05])
text_box_1 = TextBox(axbox_1, r'$\sigma_x$', initial=str(10))


axbox_2 = plt.axes([0.35, 0.01, 0.075, 0.05])
text_box_2 = TextBox(axbox_2, r'$\sigma_y$', initial=str(10))

axbox_3 = plt.axes([0.55, 0.01, 0.075, 0.05])
text_box_3 = TextBox(axbox_3, r'$\tau_{xy}$', initial=str(10))

axbox_4= plt.axes([0.75, 0.01, 0.075, 0.05])
text_box_4=TextBox(axbox_4, r'$\Theta$', initial=str(0))

text_box_4.on_submit(plot_rotated_cube)