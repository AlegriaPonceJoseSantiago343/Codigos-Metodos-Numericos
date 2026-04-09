"METODO DE LA SECANTE"
#import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4+3*x**2-2

lista_errores=[]
lista_iteraciones=[]

#MODIFICAR SEGUN EL EJERCICIO
x0=0
x1=1
tol=0.0001 #ERROR EN % MULTIPLICA x100
max_iter=50

#NO TOCAR 
Ea=100
i=1
while Ea>tol and i<max_iter:
        x2=x1-((f(x1)*(x0-x1))/(f(x0)-f(x1)))

        Ea=abs(((x2-x1)/x2)*100)
        Ea=round(Ea,5)
        lista_iteraciones.append(i)
        
        print("\nIteracion: ",i)
        print("X2 es= \n",x2)
        print("El error aproximado es:",Ea,"%")
        i+=1
        
        lista_errores.append(Ea)
        
        x0=x1
        x1=x2

plt.figure(figsize=(10,6))
plt.plot(lista_iteraciones,lista_errores,marker='o',linestyle='-',color='b',label='Error Aproximado')

plt.title("Disminucion de Error Secante")
plt.xlabel("Numero de iteracion")
plt.ylabel("Error Aprox")
plt.axhline(y=tol,color='r',linestyle='--',label=f'Tolerancia({tol})')
plt.grid(True,linestyle=':',alpha=0.7)
plt.legend()

plt.show()
