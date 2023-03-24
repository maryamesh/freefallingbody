import matplotlib.pyplot as plt
import numpy as np

# Set up the parameters of the problem
v0 = 13.0 # Initial velocity (m/s)
g = 9.8 # Acceleration due to gravity (m/s^2)

# Define a function to calculate the position of the rock at any time t
def x(t):
  return v0*t - (1/2)*g*t**2

# Generate an array of time values to plot
t = np.linspace(0, 3, 100)

# Calculate the position of the rock at each time
y = x(t)

# Plot the position of the rock as a function of time
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.show()
