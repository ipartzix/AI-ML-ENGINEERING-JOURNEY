import matplotlib.pyplot as plt
import numpy as np

# Create an array of angles
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sin and cos values
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)

# Calculate sin^2 + cos^2
sin_sq_plus_cos_sq = sin_theta ** 2 + cos_theta ** 2

# Create a figure and axes for plotting
plt.figure(figsize=(10, 5))

# Plot sin wave
plt.plot(theta, sin_theta, label='sin(theta)', color='blue')

# Plot cos wave
plt.plot(theta, cos_theta, label='cos(theta)', color='red')

# Plot sin^2 + cos^2 identity
plt.plot(theta, sin_sq_plus_cos_sq, label='sin^2(theta) + cos^2(theta)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Theta (radians)')
plt.ylabel('Value')
plt.title('Trigonometric Functions Visualization')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
