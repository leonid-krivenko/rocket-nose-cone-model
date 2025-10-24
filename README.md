# Parabolic Nose Cone Simulation

This repository contains a Python-based simulation and visualization of a **parabolic rocket nose cone**, developed as part of the **MITES Semester** engineering design project. The model generates two- and three-dimensional representations of a parabolic nose cone using analytical geometry and numerical computation.

---

## 1. Project Overview

This project was created to support the design of a water- and gas-pressure powered rocket. The goal was to analyze how the **parabolic shape factor ($K$)** affects the curvature and aerodynamic characteristics of the nose cone, thereby influencing overall rocket performance.

During this project, I investigated:
- The mathematical relationship between **shape factor**, **length**, and **radius**
- The geometric trade-offs between **parabolic**, **conical**, and **ogive** profiles
- Material and stability considerations in low-altitude flight
- The role of the nose cone in minimizing drag and maximizing altitude

---

## 2. Mathematical Model

The parabolic nose cone profile is described by the equation:

$$
y = R \cdot \frac{2(x/L) - K(x/L)^2}{2 - K}
$$

where  
- $R$ — base radius (cm)  
- $L$ — cone length (cm)  
- $K$ — shape factor (typically $0 \leq K \leq 1$)

The parameter $K$ controls the sharpness of the cone tip:  
smaller values of $K$ produce sharper tips, while larger values yield smoother, more aerodynamic shapes.

---

| Visualization | Description |
|----------------|-------------|
| <img width="638" height="659" alt="image" src="https://github.com/user-attachments/assets/03dcb96d-fd0f-4886-af08-8359acd3a9c5" /> |  *Figure 1:* 2D profile of the parabolic nose cone calculated from the analytical equation. |
| <img width="567" height="590" alt="image" src="https://github.com/user-attachments/assets/5fb97784-e368-4313-8c72-f347c0dfd0ff" /> | *Figure 2:* 3D surface of revolution of the nose cone generated using `mpl_toolkits.mplot3d`. |

Both visualizations represent the same nose-cone geometry for the chosen set of parameters.  
The 2D plot shows the curve of the profile, while the 3D rendering presents the full surface used in the rocket design.

## 7. Rocket Construction and Launch

The parabolic nose cone modeled in this simulation was physically constructed and used in the final **MITES Semester** rocket-launch project.  
The rocket was powered by compressed air and water and reached an altitude of approximately 80-100 ft during testing.

| Stage | Media |
|--------|--------|
|**Construction** | <img src="https://github.com/user-attachments/assets/b717925a-a452-4a2b-8838-8f0e7cc7d1e9" alt="Rocket" style="width:40%; height:auto;"><br><em>Figure 3: Rocket assembly phase during MITES Semester 2024.</em> |
| **Launch** | <img src="https://github.com/user-attachments/assets/042970fa-53e8-4bd0-b50c-35cb8a548aa3" alt="Rocket" style="width:40%; height:auto;"><br><em>Figure 3: Rocket assembly phase during MITES Semester 2024.</em> |
| **Flight** | <img src="https://github.com/user-attachments/assets/8fb0f89f-98f8-4992-879d-ee99f395e6d8" alt="Rocket" width="300"/> |

## 8. Future Work

This project focused on building and visualizing a parabolic nose cone model.  
There are a few ideas I want to explore next to make it more realistic and useful:

- Try modeling other shapes like **Haack** or **ogive** nose cones and compare them with the parabolic one.  
- Add some **aerodynamics** or basic **CFD** calculations to estimate drag and airflow.  
- Let the program automatically test different values of $(R, L, K)$ to see which shape gives the best flight results.  
- Include simple **material and weight estimates** to check stability and balance.  
- Build a small **interface** that lets you change parameters and instantly see how the shape changes.  
- Combine this with rocket **thrust and pressure equations** to predict flight height more accurately.

These updates would make the simulation closer to a full design and testing tool for small rockets.






