from abc import ABC  #Importamos el la libreria ABC para poder sobreescribir métodos y obliogar a las clases a tenerlo

#Creamos la clase empleado
class Empleado(ABC): 
    def __init__(self, nombre, id_empleado):   
        #Definimos sus atributos y Encapsulamos
        self.__nombre = nombre                 
        self.__id_empleado = id_empleado
    
    #Creamos un método para mostrar sus atributos    
    def atributos(self):
        print('Nombre del empleado: ', self.__nombre)
        print('Id del empleado: ', self.__id_empleado)
        
    #Creamos un método abstracto
    def calcular_salario(self):  
        pass
    
    #Creamos un getter para ver la variable nombre antes privada
    @property                
    def nombre(self):
        return self.__nombre 
    
    #Creamos un setter para modificar la variable nombre antes privada en caso de quererlo
    @nombre.setter 
    def nombre(self, valor):
        self.__nombre = valor
        

#Creamos una subclase    
class EmpleadoTiempoCompleto(Empleado):
    #Definimos sus nuevos atributos
    def __init__(self, nombre, id_empleado, salario_fijo):
        #Inicializamos los atributos ya definidos en la superclase
        super().__init__(nombre, id_empleado)
        self.salario_fijo = salario_fijo
    
    #Sobreescribimos el método calcular_salario para que actue segun la subclase    
    def calcular_salario(self): 
        print(f'El salario del empleado {self.nombre} por tiempo completo es de:', self.salario_fijo)
    
    
#Creamos una subclase
class EmpleadoPorContrato(Empleado):
    #Definimos sus nuevos atributos
    def __init__(self, nombre, id_empleado, horas_trabajadas, tarifa_por_hora):
        #Inicializamos los atributos ya definidos en la superclase
        super().__init__(nombre, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    #Sobreescribimos el método calcular_salario para que actue segun la subclase 
    def calcular_salario(self):
        salario = self.horas_trabajadas * self.tarifa_por_hora
        print(f'El salario del empleado {self.nombre} por contrato es de: {salario}') 
    
    
    
#Creamos un objeto Empleado
empleado = Empleado('Jinsonp Romario Reyes Zambrano', 'JR082698') 
#Mostramos sus atributos
empleado.atributos()

#Modificamos el atributo nombre con un setter
empleado.nombre = 'Edinson Gonzalo Reyes León' 
#Mostramos los atributos de la clase ya modificados
empleado.atributos()

#Creamos un objeto de la subclase EmpleadoTiempoCompleto
empleado_1 = EmpleadoTiempoCompleto('Bryan Santiago Reyes Zambrano', 'BR083199', 1623)
#Llamamos al método calcular salario
empleado_1.calcular_salario()

#Creamos un objeto de la subclase EmpleadoPorContrato
empleado_2 = EmpleadoPorContrato('Jefferson Steeven Reyes Zambrano', 'JR290496', 80, 3.5)
#Llamamos al método calcular salario
empleado_2.calcular_salario()

