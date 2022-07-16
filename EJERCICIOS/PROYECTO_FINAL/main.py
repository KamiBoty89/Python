"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random  # Importa libreria para aleatorio
import string  # Importa libreria para manipular cadenas
from palabras import palabras   # Importa la lista palabras del modulo palabras
# from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual  # Importa el diccionario del modulo ahorcado_diagramas
# from ahorcado_diagramas import *

def obtener_palabra_válida(palabras):         #Define funcion que recibe lista palabras, y elige una al azar  
    palabra = random.choice(palabras) 


    while '-' in palabra or ' ' in palabra:    #Mientras exista - o espacio vacio en palabra escogera una palabra al azar 
        palabra = random.choice(palabras)

    return palabra.upper()                     #Convierte palabra a mayuscula


def ahorcado():                                            #Se define la funcion ahorcado que asignara a la variable palabra una palabra aleatoria usando la funcion obtener_palabra_válida enviando la cadena palabras del mmodulo

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)               # crea una lista con cada una de las letras que forman la palabra elegida
    abecedario = set(string.ascii_uppercase)         # crea una lista con las letras del abcedario
    letras_adivinadas = set()  

    vidas = 7


    while len(letras_por_adivinar) > 0 and vidas > 0:          #Mientras la longitud de la lista sea mayor a cero y vidas mayor a cero se ejecutara

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") # nos dice que palabras llevamos formando una cadena de caracteres con el elemento de la lista

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] #recorre palabra comparando letra con cada elemento de palabra
        print(vidas_diccionario_visual[vidas])                         #imprime en pantalla lo correspondiente a la clave del diccionario del modulo
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper()   # solicita al usuario ingrese una letra y la asigna a letra usuario haciendola mayuscula

        if letra_usuario in abecedario - letras_adivinadas:   # si la letra de usuario esta en abecedario al cual se le restan las letras adivinadas es decir letras sin adivinar añade la letra a letras adivinadas
            letras_adivinadas.add(letra_usuario)
       
            if letra_usuario in letras_por_adivinar:           # si la letra esta en letras por adivinar la remueve de letras por adivinar de lo contrario resta 1 a vidas
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:           # si no esta en letras que faltan pero si en letras adivinadas nos indica que esa letra ya se escogio y de lo contrario que es invalida
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

   
    if vidas == 0:                                             # Si vidas es 0 imprime lo correspondiente a la clave 0 del diccionario del modulo vidas_diccionario_visual de lo contrario envia texto de felicitacion
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado()  #llama la funcion ahorcado