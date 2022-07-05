# 5 Práctica 5. Operadores relacionales. (6 puntos) 
### 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo

    print('Ingresa un numero')
    numero=float(input('Numero:'))
    if numero<0:
        print('El numero es negativo')
    else:
        print('El numero es positivo')  
    
### 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7

    print('Ingresa un numero')
    numero=float(input('Numero:'))
    if numero>=1 and numero<=7:
        print('El numero esta entre el rango 1-7')
    else:
        print('El numero no esta en el rango 1-7')        
    
### 5.3 Ejercicio 3 (2 puntos)
Programa si el interés es mayor al 30%, sino informa el importe total:

    print('Prestamo Facil \n Prestamos menores a $1000---> 30%' 'de interes mensual''\n Prestamos mayores o igual a $1000---> 20%' 'de interes mensual')
    print('Cual es la cantidad que desea prestada')
    cantidad=float(input('Cantidad:'))
    if cantidad<1000:
        interes=30
    else:
        interes=20      
    mensual=cantidad*(interes/100)
    print('La cantidad solicitada es de:$',cantidad)   
    print('El interes por la cantidad solicitada es de:',interes,'%') 
    print('El importe total de interes mensual:$',mensual)
