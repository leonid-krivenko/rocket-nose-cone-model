import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

R = 5.14  
L = 20.56    
K = 1     

x_vals = np.linspace(0, L, 50)

y_vals = R * ((2 * (x_vals / L) - K * (x_vals / L)**2) / (2 - K))

profile_data = pd.DataFrame({
    'x (cm)': np.round(x_vals, 2),
    'y (cm)': np.round(y_vals, 2)
})

plt.figure(figsize=(6, 6))
plt.plot(y_vals, x_vals, label="Parabolic Profile (K'=1)")
plt.gca().invert_yaxis()
plt.xlabel("Radius y (cm)")
plt.ylabel("Length x (cm)")
plt.title("Parabolic Nose Cone Profile")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()
