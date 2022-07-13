# Práctica 4. 6 puntos
## Tipos de colección de datos.
### 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo.
Respuesta:

    import random
    i=0
    numeros=[]
    while i<10:
        num=random.randint(1,10)
        numeros.append(num)  
        i=i+1  
    print(numeros)
    for n in numeros:
        print(n, 'elevado al cuadrado es:', n**2, '\n',n, 'elevado al cubo es:',n**3,'\n' )

### 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus
elementos por la pantalla.
Respuesta:

    i=0
    cadenas=[]
    cadenas2=[]
    print('Ingrese un grupo de palabras')
    while i<5:
        cadenas.append(input('Ingrese una cadena de caracteres:'))
        i=i+1  
    cadenas2.append(cadenas[::-1])    
    print(cadenas)
    print(cadenas2) 

### 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado y la menor.
Respuesta:

    import statistics
    i=0
    nota=0
    notas=[]
    print('Ingrese las notas del alumno')
    while i<5:
        nota=float(input('Ingrese nota:'))
        notas.append(nota)  
        i=i+1  
    print('Las notas del alumno son:',notas)
    print('La nota media es:',statistics.mean(notas))
    print('La nota mas alta es:',max(notas))
    print('La nota mas baja es:',min(notas))

### 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya claves
serán los nombres de los alumnos y los valores serán listados con las notas de
cada alumno.


El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al
final el programa nos mostrará la lista de alumnos y la nota media obtenida por
cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el
programa nos dará un error.
Respuesta:

    materia={}
    nombre=''
    print('Indique el numero de alumnos que desea ingresar')
    numal=int(input('Numero de alumnos:'))
    for num in range(numal):
     notas=[]   
     print('Ingrese nombre del alumno')
     nombre=input('Nombre:')
     while nombre in materia:
         print('El nombre ya existe')
         print('Ingrese nombre del alumno')
         nombre=input('Nombre:')
     nota=float(input('Ingrese la nota, ingresa una nota negativa (-) para terminar'))
     while nota>=0:
         notas.append(nota)
         nota=float(input('Ingrese la nota, ingresa una nota negativa (-) para terminar'))
         materia[nombre]=notas.copy()
    print(materia)
    for nombre,notas in materia.items():
        print(nombre,'ha obtenido las siguientes notas:',materia[nombre],'\n''Su promedio es:',sum(notas)/len(notas))

### 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero.
Respuesta:

    meses=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
    numero=int(input('Ingresa un numero, cero para terminar:'))
    while numero!=0:
        if numero<13 or numero>0:
            print(meses[numero-1])
            numero=int(input('Ingresa un numero, cero para terminar:'))
        else:
            print('Numero fuera de rango')    
            numero=int(input('Ingresa un numero, cero para terminar:'))
    print('Adios')   

# TRATA DE RESOLVER Y AVANZAR LO MÁS POSIBLE EN LOS EJERICICIOS, EL MARTES HABILITO "AYUDAS" EN CADA EJERCICIO
