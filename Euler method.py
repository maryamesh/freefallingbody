# Define the instial condtions
x0 = 200000 # Intial postion (m)
v0 = 7500   # Intial postion (m/s)
a  = -9.8   # Accelertion due to gravity (m/s^2)

# Define the time step size (s)
dt = 1

# Define the number of time steps to simulate
num_steps = 10 

# Set the intial position and velocity 
x = x0
v = v0

# Loop over the specified number of the time steps 
for i in range(num_steps):
 # Update the position and velocity using the Eular method
 x = x + v*dt
 v = v + a*dt
 
 # Print the posistion and velosity at each time step 
 print(f"Time step {i+1}: x= {x:.2f} m, v={v:.2f} m/s")
 
