# Práctica 7. Programación orientada a objetos. (6 puntos)
## Ejercicio 1 (2 puntos)
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y
DNI. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.

● mostrar(): Muestra los datos de la persona.

● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

Respuesta:

    class Persona():

        def __init__(self,nombre,edad,DNI):
         self.__nombre=nombre
         self.__edad=edad
         self.__DNI=DNI

        def getNombre(self):
            return self.__nombre

        def getEdad(self):
            return self.__edad

        def getDNI(self):
            return self.__DNI

        def setNombre(self,nom):
            self.__nombre=nom

        def setEdad(self,ed):
            self.__edad=ed

        def setDNI(self,ID):
            self.__DNI=ID              

        def Mostrar(self):
         print(f'Nombre: {self.getNombre()}')
         print(f'Edad: {self.getEdad()}')
         print(f'DNI: {self.getDNI()}')  

        def esMayorDeEdad(self):
         if self.getEdad()>=18:
                print(self.getNombre(), "es mayor de edad")
         else:
                print(self.getNombre(), "es menor de edad")  

    def Cadena(cadena):
         try:
             str(cadena)
             return True 
         except ValueError:
             return False

    def Edad(edad):
        try:
            int(edad)
            return True
        except ValueError:
            return False



    nombre=input('Ingrese nombre:')
    if Cadena(nombre):
        print('Nombre ingresado correctamente')        

    edadb=input('Ingrese edad:')

    if Edad(edadb):
        print('Edad ingresada correctamente')
    else:
        while Edad(edadb)==False:
         print('Edad ingresada erroneamente')
         edadb=input('Ingrese edad:')
        edad=int(edadb) 
        print('Edad ingresada correctamente')    

    DNI=input('Ingrese DNI:')
    if Cadena(DNI):
        print('DNI ingresado correctamente') 

    Persona1=Persona(nombre,edad,DNI) 

    Persona1.Mostrar()
    Persona1.esMayorDeEdad() 


## Ejercicio 2 (2 puntos)
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
una persona) y cantidad (puede tener decimales). El titular será obligatorio y la
cantidad es opcional. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. El atributo no se puede
modificar directamente, sólo ingresando o retirando dinero.

● mostrar(): Muestra los datos de la cuenta.

● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.

● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar
en números rojos.

Respuesta:

        class Cuenta():

            def __init__(self,titular,cantidad):
             self.__titular=titular
             self.__cantidad=cantidad

            def getTitular(self):
                return self.__titular

            def getCantidad(self):
                return self.__cantidad

            def setTitular(self,tit):
                self.__titular=tit

            def setCantidad(self,ingreso):
                self.__cantidad=ingreso

            def Mostrar(self):
             print(f'Titular: {self.getTitular()}')
             print(f'Saldo:$ {self.getCantidad()}')  

            def Ingresar(self):
             res=input('Desea ingresar dinero si/no')
             if res=='si':
                monto=float(input('Digite la cantidad a ingresar'))
                while monto<0:
                    print('Lo siento no puedes ingresar cantidades negativas, intenta de nuevo')
                    monto=float(input('Digite la cantidad a ingresar'))
                saldo=float(self.getCantidad())
                ingreso=saldo+monto
                self.setCantidad(ingreso)
             elif res=='no': 
                print('Ok, es una lastima')
             else:
                print('Respuesta equivocada.')
             print(f'Tu saldo actual es:${self.getCantidad()}')

            def Retirar(self):
             res=input('Desea retirar dinero si/no')
             if res=='si':
                monto=float(input('Digite la cantidad a retirar'))
                saldo=float(self.getCantidad())
                retiro=saldo-monto
                self.setCantidad(retiro)
             elif res=='no': 
                print('Gracias por confiar en nosotros')
             else:
                print('Respuesta equivocada.')
             print(f'Tu saldo actual es:${self.getCantidad()}')        

        titular=input('Ingrese nombre del titular:')
        cantidad=input('Ingrese cantidad de apertura:')

        Cuenta1=Cuenta(titular,cantidad) 
        Cuenta1.Mostrar()
        Cuenta1.Ingresar()
        Cuenta1.Retirar()


## Ejercicio 3 (2 puntos)
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará
expresada en tanto por ciento.Construye los siguientes métodos para la clase:

● Un constructor.

● Los setters y getters para el nuevo atributo.

● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad;, por lo tanto hay que crear un método es Titular Válido ( ) que
devuelve verdadero si el titular es mayor de edad pero menor de 25 años y
falso en caso contrario.

● Además la retirada de dinero sólo se podrá hacer si el titular es válido.

● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.

● Piensa los métodos heredados de la clase madre que hay que reescribir.
