import numpy as np
import matplotlib.pyplot as plt

# Coordenadas iniciales
A = np.array([
    (0, 0, 1),  
    (2, 0, 1),
    (0, 5, 1),
    (-2, 5, 1),
    (-4, 0, 1),
    (-2, 0, 1),
    (-1.5, 2, 1),
    (-0.5, 2, 1),
    (0, 0, 1)
])

cabecitaA = np.array([
    (-1.5, 3, 1),  
    (-0.5, 3, 1),
    (-0.75, 4, 1),
    (-1.25, 4, 1),
    (-1.5, 3, 1)
])

# Transformaciones
theta = np.pi / 6  # Rotación
R = np.array([[np.cos(theta), np.sin(theta), 0.],
              [-np.sin(theta), np.cos(theta), 0.],
              [0., 0., 1.]])

s = 5  # Escalado
S = np.array([[s, 0, 0.], [0., s, 0.], [0., 0., 1.]])

Refx = np.array([[1., 0, 0], [0, -1., 0], [0., 0., 1.]])  # Reflexión en X
Refy = np.array([[-1., 0, 0], [0, 1., 0], [0., 0., 1.]])  # Reflexión en Y

h, v = -2, 3  # Deformación horizontal y vertical
D = np.array([[1., h, 0.], [v, 1., 0.], [0., 0., 1.]])

tx, ty = -3, -5  # Traslación
T = np.array([[1., 0, tx], [0, 1., ty], [0., 0., 1.]])

transformations = {
    "Rotación": R,
    "Escalado": S,
    "Reflexión X": Refx,
    "Reflexión Y": Refy,
    "Deformación": D,
    "Traslación": T
}

# Crear subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, (name, matrix) in enumerate(transformations.items()):
    # Transformar A
    transformed_A = np.dot(A, matrix.T)
    transformed_cabecitaA = np.dot(cabecitaA, matrix.T)

    # Graficar
    ax = axes[idx]
    ax.plot(A[:, 0], A[:, 1], color="blue", label="Original")
    ax.plot(cabecitaA[:, 0], cabecitaA[:, 1], color="blue")
    ax.plot(transformed_A[:, 0], transformed_A[:, 1], color="red", label="Transformado")
    ax.plot(transformed_cabecitaA[:, 0], transformed_cabecitaA[:, 1], color="red")
    ax.set_title(name)
    ax.set_aspect('equal', adjustable='box')
    ax.grid()
    ax.legend()

# Ajustar diseño
plt.tight_layout()
plt.show()
