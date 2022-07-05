## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.

       print('Indica el valor en grados Fahrenheit')
       far=int(input('Grados fahrenheit:'))
       cen=(far-32)*5/9  
       print(far,'°F son ',cen, '°C')

2.2 Ejercicio 2 (1.5 puntos)

Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.

    print('Ingresa un numero')
    num1=int(input('Primer numero:'))
    print('Ingresa otro numero')
    num2=int(input('Segundo numero:'))
    suma=num1+num2
    resta=num1-num2
    mult=num1*num2
    div=num1/num2
    print('La suma de ',num1,'y',num2,'es:',suma)
    print('La resta de ',num1,'y',num2,'es:',resta)
    print('La multiplicación de ',num1,'y',num2,'es:',mult)
    print('La división de ',num1,'y',num2,'es:',div)

2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

    print('Programa que calcula el périmetro y área de un rectangulo')
    print('Ingresa la base del rectangulo')
    base=int(input('Base:'))
    print('Ingresa la altura del rectangulo')
    altura=int(input('Altura:'))
    perimetro=(2*base)+(2*altura)
    area=base*altura
    print('El périmetro del rectangulo es  ',perimetro,'u')
    print('El área del rectangulo es ',area,'u2')

