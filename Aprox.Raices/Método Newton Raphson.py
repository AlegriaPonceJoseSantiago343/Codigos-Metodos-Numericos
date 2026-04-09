"NEWTON RAPHSON"
import sympy as sp
import matplotlib.pyplot as plt

lista_errores=[]
lista_iteraciones=[]


def NewtonRaphson(x0,tol,n):
    x=sp.symbols("x")#declaramos x como un simbolo y no como una variable normal
    f=input("digite la funcion con variable x:\n")
    
    df=sp.diff(f)#la libreria sympy calcula la derivada 
    f=sp.lambdify(x,f)#lambdify transforma la variable simbolica en una manejable por py 
    df=sp.lambdify(x,df)
    
    for k in range(n):#el ciclo se repetira n veces segun se configure
        x1=x0-f(x0)/df(x0)#formula de nwethon raphson
        Ea=abs(((x1-x0)/x1)*100)
        Ea=round(Ea,5)
        
        lista_errores.append(Ea)
        lista_iteraciones.append(k)
        
        
        if(abs(x1-x0)<tol):#si la diferencia es menor a la tolerancia se detiene
            print("\nx",k+1,"=",x1,end=" ")
            print("Ea:",Ea,"%")
            print("es una buena aproximacion de la raiz")
            return
        
        x0=x1#si se necesitan mas iteraciones x0 toma nuevos valores para la sig iteracion
        print("\nx",k+1,"=",x1)
        print("Error Aprox:",Ea,"%")

#EL PUNTO INICIAL NO DEBE SER 0 SINO DA ERROR DE DIVISION DE CEROS
NewtonRaphson(0.1,0.000001,30)
#x0,tolerancia NORMAL sin %,numero de iteraciones

plt.figure(figsize=(10,6))
plt.plot(lista_iteraciones,lista_errores,marker='o',linestyle='-',color='b',label='Error Aproximado')
 
plt.title("Disminucion de Error Newton Raphson")
plt.xlabel("Numero de iteracion")
plt.ylabel("Error Aprox")
#IMPORTANTE modificar la tolerancia segun el ejercicio (Es para la linea roja de la grafica)
plt.axhline(y=1,color='r',linestyle='--',label=f'Tolerancia({0.01})')
plt.grid(True,linestyle=':',alpha=0.7)
plt.legend()
plt.show()
