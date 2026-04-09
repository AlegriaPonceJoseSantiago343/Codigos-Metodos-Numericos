"METODO FALSA POSICION"
#import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return  x**4+3*x**2-2

#Modificar segun el ejercicio
a=0.1
b=3
tol=0.0001 #En porcentaje
max_iter=30

#No tocar (es para que el code se inicie y el contador)
Ea=100
i=1
x_anterior=0

lista_errores=[]
lista_iteraciones=[]

if f(a)*f(b)<=0:
   while Ea>tol and i<max_iter:
     
    print("\n---Los intervalos cumplen bolzano---\n")
         
    x1=b-(f(b)*(a-b)/(f(a)-f(b)))

    if i>1:
        Ea=abs(((x1-x_anterior)/x1)*100)
        Ea=round(Ea,5)
        
        lista_errores.append(Ea)
        lista_iteraciones.append(i)
        
    else:
        print("---")
    
    print("\nIteracion: ",i,)
    #print("FA=",f(a))
    #print("FB=",f(b))
    print("X1=",x1)
    print("Ea:",Ea,"%")
    if Ea<tol:
        print("---Llegamos al valor permitido---")
    x_anterior = x1
    i+=1
    
    if f(x1)>0:
        a=x1
    else:
        b=x1
        
    plt.figure(figsize=(10,6))
    plt.plot(lista_iteraciones,lista_errores,marker='o',linestyle='-',color='b',label='Error Aproximado')
    
    plt.title("Disminucion de Error Falsa Posicion")
    plt.xlabel("Numero de iteracion")
    plt.ylabel("Error Aprox")
    plt.axhline(y=tol,color='r',linestyle='--',label=f'Tolerancia({tol})')
    plt.grid(True,linestyle=':',alpha=0.7)
    plt.legend()
    plt.yscale('log')
    plt.show()
    
else:
    print("La raiz no esta en ese intervalo")
        
        
    
