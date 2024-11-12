import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
plt.ioff()  # Turns off interactive mode

# Constants
delta = 0 # Example value for delta

# Define the Bloch equations
def blocheqns(t, y):  # Only `delta` is an extra argument here
    u, v, w = y  # y contains [u, v, w]
    du_dt = delta * v
    dv_dt = w - delta * u 
    dw_dt = -v
    return [du_dt, dv_dt, dw_dt]


# Initial conditions for u, v, w
u0 = 0.0
v0 = 1.0
w0 = 0.0
initial_conditions = [u0, v0, w0]

# Time span and points for evaluation
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system of ODEs
solution = solve_ivp(blocheqns, t_span, initial_conditions, t_eval=t_eval)

# Extract the results
u_sol = solution.y[0]
v_sol = solution.y[1]
w_sol = solution.y[2]

# Create a 3D plot of the trajectory
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot u, v, w as a function of time in 3D space
ax.plot(u_sol, v_sol, w_sol)
ax.set_xlabel("u(t)")
ax.set_ylabel("v(t)")
ax.set_zlabel("w(t)")
ax.set_title("3D Trajectory of (u, v, w) as a function of time")

ax.quiver(0, 0, 0, 1, 0, delta, color='g', label="Precession vector", arrow_length_ratio=0.1)


# Unit sphere
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)


x_sphere = np.sin(theta) * np.cos(phi)
y_sphere = np.sin(theta) * np.sin(phi)
z_sphere = np.cos(theta)

ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.1, rstride=5, cstride=5, edgecolor='w')
max_range = 1.2

ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])


# Axes
ax.set_box_aspect([1, 1, 1])  # Aspect ratio 1:1:1
ax.grid(False)
ax.w_xaxis.pane.set_visible(False)
ax.w_yaxis.pane.set_visible(False)
ax.w_zaxis.pane.set_visible(False)


ax.plot([-max_range, max_range], [0, 0], [0, 0], color="black", linestyle="--")  # x-axis
ax.plot([0, 0], [-max_range, max_range], [0, 0], color="black", linestyle="--")  # y-axis
ax.plot([0, 0], [0, 0], [-max_range, max_range], color="black", linestyle="--")  # z-axis

plt.show()