
# 2D Stress Transformation and Rotated Cube Visualization

This Python project visualizes 2D stress transformation and the corresponding rotated 2D cube under stress. It allows the user to input normal and shear stress values along with a rotation angle and dynamically visualizes how the stress transforms and how the 2D element (cube) rotates accordingly.

## Features

- **Stress Transformation**: Computes the transformed normal and shear stresses for a 2D element under a given rotation.
- **Dynamic Visualization**: A 2D square (representing a material element) is drawn, and based on the user's inputs, it rotates to reflect the stress transformation.
- **Interactive Input**: Uses `matplotlib`'s `TextBox` widget to allow user input for the following:
  - Normal stress in the x-direction (`σ_x`)
  - Normal stress in the y-direction (`σ_y`)
  - Shear stress (`τ_xy`)
  - Rotation angle (`θ` in degrees)
- **Shear and Normal Stress Visualization**: Arrows are drawn on the edges of the 2D element to show the directions and magnitudes of shear and normal stresses, with red arrows representing shear stress and black arrows for normal stress.
- **Rotation Angle Display**: The program shows the angle of rotation using an arc and annotates the resulting stress values directly on the plot.

## How It Works

1. The user enters values for `σ_x`, `σ_y`, `τ_xy`, and `θ` (in degrees) via input boxes displayed below the plot.
2. When a new value for the rotation angle is submitted, the plot dynamically updates to show:
   - The rotated 2D cube (representing the material element).
   - The transformed normal and shear stresses.
   - Arrows representing the direction and magnitude of both normal and shear stresses.
   - The rotation angle is displayed as an arc on the plot.
3. The transformation is computed using the following equations:
   - Transformed normal stresses (`σ_x'` and `σ_y'`):
     ```
     σ_x' = σ_x * cos²(θ) + σ_y * sin²(θ) + 2 * τ_xy * sin(θ) * cos(θ)
     σ_y' = σ_x * sin²(θ) + σ_y * cos²(θ) - 2 * τ_xy * sin(θ) * cos(θ)
     ```
   - Transformed shear stress (`τ_xy'`):
     ```
     τ_xy' = (σ_y - σ_x) * sin(2θ) / 2 + τ_xy * cos(2θ)
     ```

## Prerequisites

To run this project, you'll need to install the following Python packages:

- **matplotlib**: Used for plotting and visualizing the rotated cube and stress transformations.
- **numpy**: Used for performing mathematical operations like trigonometry and square roots.

You can install these packages using `pip`:

```bash
pip install matplotlib numpy
```

## Usage

1. Clone this repository or download the script.
2. Run the script using any Python environment that supports interactive plots (e.g., Jupyter, VSCode, or directly using a Python interpreter with `matplotlib` backend enabled).

To run the script:

```bash
python stress_transformation_visualization.py
```

The script will open a window with an interactive plot and input boxes for `σ_x`, `σ_y`, `τ_xy`, and `θ`. You can modify these values, and the plot will update automatically.

## Input Parameters

- **`σ_x`**: Normal stress acting in the x-direction.
- **`σ_y`**: Normal stress acting in the y-direction.
- **`τ_xy`**: Shear stress acting on the xy-plane.
- **`θ`**: The angle of rotation of the element (in degrees).

## Example

For an element with:

- `σ_x = 20 MPa`
- `σ_y = 10 MPa`
- `τ_xy = 5 MPa`
- `θ = 30°`

The plot will show:

- The rotated 2D element (cube).
- Transformed stresses (`σ_x'`, `σ_y'`, `τ_xy'`).
- Arrows for both normal and shear stresses on the cube.
- The arc indicating the rotation angle of 30°.

## Screenshots

![image](https://github.com/user-attachments/assets/16ff9981-7723-4128-b100-b883584f34b7)

![image](https://github.com/user-attachments/assets/cbdb834b-a4f2-4ad8-a6e7-590828f26840)

![Figure 14](https://github.com/user-attachments/assets/98f95207-b3f0-4cf2-a2b0-bb1c2764f293)


## Acknowledgments

This project was built using Python's `matplotlib` and `numpy` libraries. It provides a visual and intuitive way to understand stress transformations in 2D elements, commonly used in mechanics of materials and civil/structural engineering applications.

---

### License

Feel free to modify and use this project for educational purposes or as a starting point for more complex stress analysis visualizations.

---

## Troubleshooting

- Ensure you have all the required libraries installed. If you encounter any issues with the interactive plot, try running the script in a Jupyter notebook or using an interactive Python environment.

---

