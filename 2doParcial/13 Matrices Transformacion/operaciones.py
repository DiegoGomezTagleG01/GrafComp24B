import numpy as np

# Definimos las matrices y puntos
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

# 1. Matriz de Rotación
theta = np.pi / 6  # Ángulo de rotación
R = np.array([
    [np.cos(theta), np.sin(theta), 0],
    [-np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

# 2. Matriz de Escalado
s = 5  # Factor de escala
S = np.array([
    [s, 0, 0],
    [0, s, 0],
    [0, 0, 1]
])

# 3. Matriz de Reflexión en el eje X
Refx = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

# Función para mostrar las operaciones paso a paso
def mostrar_operaciones(matriz, puntos, nombre_transformacion, nombre_matriz):
    print(f"\nTransformación: {nombre_transformacion} ({nombre_matriz})")
    for i, punto in enumerate(puntos):
        print(f"\nPunto original {i + 1}: {punto}")
        resultado = matriz @ punto
        print(f"Multiplicación paso a paso:")
        for fila, valor in zip(matriz, resultado):
            print(f"  {fila} . {punto} = {valor}")
        print(f"Resultado transformado: {resultado[:-1]}")  # Excluye la última coordenada homogénea

# Aplicar y mostrar las operaciones para ambas matrices
for matriz, nombre_matriz in [(A, "A"), (cabecitaA, "cabecitaA")]:
    #mostrar_operaciones(R, matriz, "Rotación", nombre_matriz)
    #print(np.dot(A, R))
    #mostrar_operaciones(S, matriz, "Escalado", nombre_matriz)
    #print(np.dot(A, S))
    mostrar_operaciones(Refx, matriz, "Reflexión en el eje X", nombre_matriz)
    print(np.dot(A, Refx))
