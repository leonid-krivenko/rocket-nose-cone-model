import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 5.5
L = 25.5
K = 1

x_vals = np.linspace(0, L, 50)

y_vals = R * ((2 * (x_vals / L) - K * (x_vals / L)**2) / (2 - K))

theta = np.linspace(0, 2 * np.pi, 50)
X, Theta = np.meshgrid(x_vals, theta)

Y = R * ((2 * (X / L) - K * (X / L)**2) / (2 - K))
Z = Y * np.cos(Theta)
W = Y * np.sin(Theta)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(W, Z, X, cmap='viridis', edgecolor='k', linewidth=0.1, alpha=0.9)

ax.set_title("3D Parabolic Nose Cone (Realistic View)")
ax.set_xlabel("Width X (cm)")
ax.set_ylabel("Width Y (cm)")
ax.set_zlabel("Length (cm)")

max_range = np.array([W.max() - W.min(), Z.max() - Z.min(), X.max() - X.min()]).max() / 2.0
mid_x = (W.max() + W.min()) * 0.5
mid_y = (Z.max() + Z.min()) * 0.5
mid_z = (X.max() + X.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.view_init(elev=15, azim=110)

plt.tight_layout()
plt.show()
