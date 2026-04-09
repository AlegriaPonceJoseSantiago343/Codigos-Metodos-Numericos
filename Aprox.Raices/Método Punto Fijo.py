"PUNTO FIJO"
import numpy as np
import matplotlib.pyplot as plt

#DEBES ANOTAR SOLO LA --TRANSFORMACION-- DE LA FUNCION
def f(x):
    return np.sqrt((2-x**4)/3)

lista_errores=[]
lista_iteraciones=[]

 #MODIFICAR SEGUN EL EJERCICIO
x0=0.1
Ea=100
#tolerancia de error en porcentaje
tol=0.0001  

i=1
max_iter=30

while Ea>tol and i<max_iter:
    
    x1=f(x0)
    Ea=abs(((x1-x0)/x1)*100)
    Ea=round(Ea,5)
    lista_iteraciones.append(i)
    lista_errores.append(Ea)
    
    print("\nIteracion: ",i)
    print("X1=",x1)
    print("Error aproximado:",Ea,"%")
    x0=x1
    i+=1
    
plt.figure(figsize=(10,6))
plt.plot(lista_iteraciones,lista_errores,marker='o',linestyle='-',color='b',label='Error Aproximado')

plt.title("Disminucion de Error Punto Fijo")
plt.xlabel("Numero de iteracion")
plt.ylabel("Error Aprox")
plt.axhline(y=tol,color='r',linestyle='--',label=f'Tolerancia({tol})')
plt.grid(True,linestyle=':',alpha=0.7)
plt.legend()
plt.yscale('log')
plt.show()
