import matplotlib.pyplot as plt
#import numpy as np
def f(x):
    return x**4+3*x**2-2

#insertamos la funcion

lista_errores=[]
lista_iteraciones=[]

def biseccion(a, b, tol):#creamos las variables 
    m1 = a
    m = b
    k = 0
    
 #verificamos que cambie signo para poder hacer la biseccion
    if f(a) * f(b) > 0:
        print("La función no cambia de signo en este intervalo.")
        return 

    ##mientras que no sea menor que la tolerancia el proceso se repite 
    while abs(m1 - m) > tol:
        m1 = m#formulas del metodo de biseccion
        m = (a + b) / 2  
        #ocurren dos casos dependiendo el reultado de la multipliacion
        if f(a) * f(m) < 0:
            b = m
        elif f(m) * f(b) < 0: 
            a = m
        #se suma un uno al numero total de iteraciones
        k += 1  
        
        lista_iteraciones.append(k)
        
        Ea=abs(((a-b)/a)*100)
        Ea=round(Ea,5)
        lista_errores.append(Ea)
        
        print(f"Iteración {k}: el intervalo es [{a:.4f}, {b:.4f}]")
        print(f"x{k} = {m:.4f}")
        print(f"Error Aprox: {Ea}\n")
    
    plt.figure(figsize=(10,6))
    plt.plot(lista_iteraciones,lista_errores,marker='o',linestyle='-',color='b',label='Error Aproximado')
    
    plt.title("Disminucion de Error Biseccion")
    plt.xlabel("Numero de iteracion")
    plt.ylabel("Error Aprox")
    plt.axhline(y=tol,color='r',linestyle='--',label=f'Tolerancia({tol})')
    plt.grid(True,linestyle=':',alpha=0.7)
    plt.legend()
    
    plt.show()

biseccion(0.1,3, 0.0001)
#Valor de A , Valor de B, Tolerancia normal
#Procura no anadir ceros 
