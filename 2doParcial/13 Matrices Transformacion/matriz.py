import numpy as np
import matplotlib .pyplot as plt

E = np.array ([(0 ,0 ,1) ,(3,0,1) ,(3,1,1) ,(1,1,1) ,(1,2,1) ,(2,2,1),
(2 ,3 ,1) ,(1,3,1) ,(1,4,1) ,(3,4,1) ,(3,5,1) ,(0,5,1),(0,0,1)])

# Matriz Identidad
Ic = np.eye (3)

#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi/3 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = -3
ty = -5
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (R.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()





#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi*3/2 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = -3
ty = -5
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (R.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()




#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi*3/2 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = -3
ty = -5
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (Refy.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()






#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi*3/2 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = -3
ty = -5
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (S.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()






#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi*3/2 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = -3
ty = -5
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (D.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()



#Matriz de Reflexión con respecto al eje x
Refx=np.array ([[1. , 0, 0],[0, -1., 0] ,[0. , 0., 1.]])
#Matriz de Reflexión con respecto al eje y
Refy=np.array([[-1., 0, 0],[0, 1., 0] ,[0. , 0., 1.]])
# Matriz de Rotación
theta= np.pi*3/2 #Ángulo de rotación deseado ,en este caso usamos pi/3.
R=np.array ([[ np.cos(theta), np.sin(theta), 0.],
[-np.sin(theta), np.cos(theta), 0.],
[0., 0., 1.]])
# Matriz de cambio de escala
s=2 #Escalar
S=np.array ([[s, 0, 0.], [0., s, 0.] ,[0. , 0., 1.]])
# Matriz de deformación horizontal/vertical
h=-1
v= 2
D=np.array ([[1. , h, 0.] ,[v, 1., 0.] ,[0. , 0., 1.]])
# Matriz de traslación
tx = 3
ty = 0
T=np.array ([[1. , 0, tx], [0, 1., ty], [0., 0., 1.]])
#transformación y plot
ax = plt.gca () #gca= get current axes , obtiene los ejes actuales
Ex = [] #Lista de primeras componentes
Ey = [] #Lista de segundas componentes
for row in E:
    output_rown = (T.dot(row)) #Multiplicación de la matriz por el punto respectivo
    
    x, y, _= output_rown #Coordenadas ya transformadas
    Ex.append(x) #Se guardan las coordenadas
    Ey.append(y)
plt.plot(E[:,0], E[:,1], color="blue") #Se grafica E sin transformar
plt.plot(Ex , Ey , color="Red") #Se grafica E transformada
ax. set_xticks (np.arange(-6, 8, 2)) # Fija el rango del eje x
ax. set_yticks (np.arange(-6, 8, 2)) # Fija el rango del eje y
plt.gca (). set_aspect ('equal', adjustable ='box') #Establece misma escala
plt.grid () #Habilita la cuadrícula
plt.show()