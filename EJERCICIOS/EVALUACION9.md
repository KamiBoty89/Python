# Práctica 9. Programación funcional. (6 puntos)
## Ejercicio 1 (2 puntos)
Realice un programa que pregunte aleatoriamente una multiplicación. El programa
debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea
incorrecta el programa debe indicar cuál es la correcta). El programa preguntará
10 multiplicaciones, y al finalizar mostrará el número de aciertos.

#### Análisis
* Hacemos un bucle con 10 iteraciones, en cada iteración se inicializan dos
números con un valor aleatorio (de 2 a 10). Se calcula la multiplicación.
* Mostramos la multiplicación, y pedimos por teclado el resultado. Si
coincide con la multiplicación calculada cuento un acierto, sino escribimos un
mensaje de error mostrando el resultado correcto. Cuando salimos del bucle
mostramos el número de aciertos.

Ejemplo. imprime una multiplicacion (9 * 8 =  )por teclado se ingresa la respuesta, eso pasa 10 veces y al final nos imprime cuantas respuestas fueron correctas

Recuerda el import random

Respuesta:

    import random
    total=0
    for n in range(10):
     n1= random.randint(2, 10)
     n2= random.randint(2, 10)
     res=n1*n2
     print('¿Cuanto da el producto de',n1,'*',n2,'es tu respuesta?')
     resus=int(input('R='))
     if resus==res:
         print('¡¡¡CORRECTO!!!')
         total=total+1
     else:    
         print('¡¡¡INCORRECTO!!!')
    print('Acertaste',total,'veces.') 

## Ejercicio 2 (2 puntos)
Obtener el cuadrado de todos los elementos en la lista.

Lista: [1,2,3,4,5,6,7,8,9,10]

Respuesta:

        Lista=[1,2,3,4,5,6,7,8,9,10]
        for n in range(len(Lista)):
         print(Lista[n],'elevado al cuadrado es:',Lista[n]**2)

## Ejercicio 3 (2 puntos)
Obtener la cantidad de elementos mayores a 5 en la tupla.

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

Respuesta:

        tupla=(5,2,6,7,8,10,77,55,2,1,30,4,2,3)
        total=0
        lista=[]
        for n in range(len(tupla)):
            if tupla[n]>5:
                total=total+1
                lista.append(tupla[n])
        print('Hay',total,'elementos mayores a 5 en la tupla y son:',lista)

## Ejercicio 4 (2 puntos)
Obtener la suma de todos los elementos en la lista

lista = [1,2,3,4]

Respuesta:

        lista=[1,2,3,4]
        suma=0
        for n in range(len(lista)):
             suma=suma+lista[n]
        print('La suma de los numeros de la lista es:',suma)

