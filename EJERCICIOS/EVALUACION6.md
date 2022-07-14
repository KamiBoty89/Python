# 6 Práctica 
Sentencias condicionales. (6 puntos)

## Ejercicio 1 (1.5 puntos)
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.

Menú de recomendaciones
1. Literatura
2. Cine
3. Música
4. Videojuegos
5. Salir

### Al ingresar una opcion
opcion 1:

Lecturas recomendables:

* Esperándolo a Tito y otros cuentos de fútbol (Eduardo
Sacheri)
* El juego de Ender (Orson Scott Card)
* El sueño de los héroes (Adolfo Bioy Casares)

opcion 2:

Películas recomendables:

* Matrix (1999)
* El último samuray (2003)
* Cars (2006)

opcion  3:

Discos recomendables:

* Despedazado por mil partes (La Renga, 1996)
* Búfalo (La Mississippi, 2008)
* Gaia (Mago de Oz, 2003)

opcion 4:

* Videojuegos clásicos recomendables
* Día del tentáculo (LucasArts, 1993)
* Terminal Velocity (Terminal Reality/3D Realms, 1995)
* Death Rally (Remedy/Apogee, 1996)

opcion  5:

Gracias, vuelva prontos

Opción no válida, en caso de ingresar un número fuera de las opciones

Respuesta:

    while True:
      eleccion = input("""
       1 - Literaura
       2 - Cine
       3 - Música
       4 - Videojuegos
       5 - Salir
       Selecciona una opción: """)

      if eleccion == "1":
         print('Lecturas recomendables:\n  °Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)\n  °El juego de Ender (Orson Scott Card)\n  °El sueño de los héroes (Adolfo Bioy Casares)')

      elif eleccion == "2":
         print('Películas recomendables:\n  °Matrix (1999)\n  °El último samuray (2003)\n  °Cars (2006)')

      elif eleccion == "3":
         print('Discos recomendables:\n  °Despedazado por mil partes (La Renga, 1996)\n  °Búfalo (La Mississippi, 2008)\n  °Gaia (Mago de Oz, 2003)')

      elif eleccion == "4":
         print('Videojuegos clásicos recomendables:\n  °Día del tentáculo (LucasArts, 1993)\n  °Terminal Velocity (Terminal Reality/3D Realms, 1995)\n  °Death Rally (Remedy/Apogee, 1996)')

      elif eleccion == "5":
           print('Gracias, vuelva prontos')
           break
      else:
        print('Opción invalida')

## Ejercicio 2 (1.5 puntos)
Se pide por teclado un número y nos imprime los números primos que hay previos a este número.

Ejemplo: si ingresamos el 10 nos imprima del 1 a ese 10 cuales números son primos.

Respuesta:

        print('Ingressa un numero entero positivo')
        numero=int(input('Numero:'))
        j=1
        lista2=[]
        while j<=numero:
         lista=[]
         i=1   
         while i<=j:
             if j%i==0:
                 lista.append(i)    
             i=i+1  
         if len(lista)<=2:
             lista2.append(j)
         j=j+1         
        print('Los numeros primos entre el numero 1 y el numero',numero, 'son:',lista2)     

## Ejercicio 3 (1.5 puntos)
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de lo que pagó
después de los 20 meses.

Al finalizar los 20 meses pago en total:

primer mes pago 10, segundo mes pago 20, tercer mes pago 30, cuarto mes pago 40, etc.
