import matplotlib.pyplot as plt
# Set the initial conditions
x0 = 0  # Initial position (m)
y0 = 0  # Initial height (m)
vx0 = 0  # Initial velocity in the x-direction (m/s)
vy0 = 0  # Initial velocity in the y-direction (m/s)
# Set the time step and duration of the simulation
dt = 0.01  # Time step (s)
t_max = 10  # Duration of the simulation (s)
# Set the acceleration due to gravity (m/s^2)
g = 9.81
# Create lists to store the results
t_values = []  # Time values
x_values = []  # Positions in the x-direction
y_values = []  # Positions in the y-direction
# Set the initial time and positions
t = 0
x = x0
y = y0
# Set the initial velocities
vx = vx0
vy = vy0
# Use the Euler method to simulate the free fall
while t < t_max:
    # Append the current time and positions to the lists
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)
    # Update the velocity in the y-direction using the acceleration due to gravity
    vy += -g * dt
    # Update the position using the velocity
    x += vx * dt
    y += vy * dt
    # Update the time
    t += dt
# Plot the results
plt.plot(x_values, y_values)
plt.xlabel('Position in the x-direction (m)')
plt.ylabel('Position in the y-direction (m)')
plt.show()