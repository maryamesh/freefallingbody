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

# Use the Runge-Kutta method to simulate the free fall
while t < t_max:
    # Append the current time and positions to the lists
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)

    # Calculate the intermediate values
    k1_vx = vx * dt
    k1_vy = vy * dt
    k2_vx = (vx + k1_vx/2) * dt
    k2_vy = (vy + k1_vy/2 - g * dt/2) * dt
    k3_vx = (vx + k2_vx/2) * dt
    k3_vy = (vy + k2_vy/2 - g * dt/2) * dt
    k4_vx = (vx + k3_vx) * dt
    k4_vy = (vy + k3_vy - g * dt) * dt
    
    # Update the velocity using the intermediate values
    vx += (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
    vy += (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6
    
    # Update the position using the average of the initial and final velocities
    x += (vx + vx + dt) / 2 * dt
    y += (vy + vy + dt) / 2 * dt

    # Update the time
    t += dt

# Plot the results
plt.plot(x_values, y_values)
plt.xlabel('Position in the x-direction (m)')
plt.ylabel('Position in the y-direction (m)')
plt.show()