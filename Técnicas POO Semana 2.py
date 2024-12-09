from abc import ABC #Importamos ABC para crear la clase abstracta

class Vehiculo(ABC): #Llamamos ABC para crear la encapsulación
    def __init__(self, marca, modelo, año): #Establecemos los atributos de la clase madre (Abstracción)
        self.__marca = marca #Encapsulamos los atributos con __ 
        self.__modelo = modelo
        self.__año = año
   
    
    def atributos(self): 
        print(self.__marca, ':', sep='')
        print('. Modelo:', self.__modelo)
        print('. Año:', self.__año)
        

class Auto(Vehiculo): #Creamos una clase hija (Herencia)
    
    def __init__(self, marca, modelo, año, puertas): #Le añadimos el atributo puertas
        super().__init__(marca, modelo, año) #Inicializamos el constructor de la clase madre
        self.puertas = puertas #Le asignamos un valor a puertas
    
    def atributos(self): #Modificamos la función atributos para que ahora también muestre el atributo puertas
        super().atributos() 
        print('. Tipo auto:', self.puertas, 'puertas.')
        
    @property #Hacemos un getter para que me permita ver el atributo encapsulado
    def puertas(self): 
        return self.__puertas    

    @puertas.setter #Hacemos un setter para que me permita modificar el atributo encapsulado
    def puertas(self, valor):
        self.__puertas = valor
        
class Moto(Vehiculo): #Repetimos los pasos de la subclase Auto
    
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.__tipo = tipo
        
    def atributos(self):
        super().atributos()
        print('. Tipo moto:', self.tipo)
        
    @property
    def tipo(self):
        return self.__tipo    

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor


vehiculo_1 = Auto('Suzuki', 'JIMNY', '2024', 5) #Creamos el primer objeto
vehiculo_1.atributos() #Mostramos sus atributos

vehiculo_2 = Moto('Yamaha', 'R15 V4', '2022', 'Deportiva') #Creamos un segundo objeto
vehiculo_2.atributos() #Mostramos sus atributos

vechiculos = [Auto('Suzuki', 'JIMNY', '2024', 5), Moto('Yamaha', 'R15 V4', '2022', 'Deportiva') ] #Aplicamos el polimorfismo

for vehiculo in vechiculos: #Mostramos los atributos de dos clases distintas, el mismo método atributos actua diferente según el objeto
    vehiculo.atributos()

  
print(vehiculo_1.puertas) #Verificamos que podemos visualizar el atributo puertas encapsulado

vehiculo_2.tipo = 'Urbana'#Verificamos que podemos modificar el atributo tipo, encapsulado

vehiculo_2.atributos() # Verificamos que se modificó el atributo tipo, encapsulado