import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
plt.ioff()  # Turns off interactive mode

# Define the Bloch equations
def blocheqns(t, y, delta):  # Only `delta` is an extra argument here
    u, v, w = y  # y contains [u, v, w]
    du_dt = delta * v
    dv_dt = -delta * u + 1
    dw_dt = -u
    return [du_dt, dv_dt, dw_dt]

# Constants
delta = 0.5  # Example value for delta

# Initial conditions for u, v, w
u0 = 0.0
v0 = 1.0
w0 = 0.0
initial_conditions = [u0, v0, w0]

# Time span and points for evaluation
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system of ODEs
solution = solve_ivp(blocheqns, t_span, initial_conditions, args=(delta,), t_eval=t_eval)

# Extract the results
u_sol = solution.y[0]
v_sol = solution.y[1]
w_sol = solution.y[2]

# Create a 3D plot of the trajectory
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot u, v, w as a function of time in 3D space
ax.plot(u_sol, v_sol, w_sol, label='Trajectory (u, v, w) over time')
ax.set_xlabel("u(t)")
ax.set_ylabel("v(t)")
ax.set_zlabel("w(t)")
ax.set_title("3D Trajectory of (u, v, w) as a function of time")
ax.legend()

plt.show()
