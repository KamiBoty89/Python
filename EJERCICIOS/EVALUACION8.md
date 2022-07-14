# Práctica 8. (6 puntos)
## Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un
diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
valores sean los cuadrados de las claves.

Ejemplo: si se ingresa el 4 imprima el cuadrado de 1, de 2, de 3 y de 4

Respuesta:

    print('Ingresa un nuero entero positivo')
    numero=int(input('Numero:'))
    diccionario={}
    for num in range(numero):
        diccionario[num+1]=(num+1)**2
        print('El cuadrado de',num+1,'es:',diccionario[num+1])



## Ejercicio 2 (2 puntos)
Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada carácter en la cadena.

Ejemplo: si se ingresa "paloma" p=1 a=2 l=1 o=1 m=1

Respuesta:

        print('Ingresa una palabra')
        cadena=input('Palabra:')
        cadena2=[]
        palabra={}
        for i in range(len(cadena)):
            if cadena[i] not in cadena2:
             cadena2.append(cadena[i])
        for j in range(len(cadena2)):
            h=0
            for k in range(len(cadena)):
              if cadena[k]==cadena2[j]:
                 h=h+1
              palabra[cadena2[j]]=h        
        print('La palabra '+cadena+' contiene:',palabra)

## Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta
y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de
los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras
cada consulta el programa nos preguntará si queremos hacer otra consulta.
