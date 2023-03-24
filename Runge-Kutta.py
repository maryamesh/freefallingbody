## Define the initial position (m)
x0 = 200000 # Intial postion (m)
v0 = 7500   # Intial postion (m/s)
a  = -9.8   # Accelertion due to gravity (m/s^2)
# Define the time step size (s)
dt = 1
# Define the number of time steps to simulate
num_steps = 10
# Set the initial positon and velocity
x = x0
v = v0
# Loop over the specified number of the time steps
for i in range(num_steps):
    # calculate the position and velocity at the midpoint of the time step using the Euler method
    x_mid = x + v*dt/2
    v_mid = v + a*dt/2
    # Calculate the acceleration at the midpoint of the time step using the equation of motion
    a_mid = a
    # Update the position and velocity using the improved Euler method
    x = x + v_mid*dt
    v = v + a_mid*dt
    # Calculate the acceleration at the end of the time step using the equation of motion
    a_end = a
    v_end = v
    # Update the position and velocity using the fourth-order Runge-Kutta method
    x = x + dt/6*(v + 2*v_mid + 2*v_end + v)
    v = v + dt/6*(a + 2*a_mid + 2*a_end + a)
    # print the position and velocity at each time step
    print(f"Time step {i+1}: x= {x:.2f} m, v={v:.2f} m/s")





