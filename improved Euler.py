# Define the initial position (m)
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
    # Calculate the acceleration at the current time step using the equation of motion
    a_current = a
    # calculate the position and velocity at the midpoint of the time step using the Eular method
    x_mid = x + v*dt/2
    v_mid = v + a_current*dt/2
    # Caclculate the acceleration at the midpoint of the time step using the equation of motion
    a_mid = a
    # Update the position and velocity using the improved Euler method
    x = x + v_mid*dt
    v = v + a_mid*dt
    # print the position and velocity at each time step
    print(f"Time step {i+1}: x= {x:.2f} m, v={v:.2f} m/s")




