class Auto:
    def __init__(self, marca, modelo, año): #Creamos el objeto auto y le damos atributos
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.rentado = False   

    def rentar(self): #Verifica si se puede rentar el auto
        if not self.rentado:
            self.rentado = True
            return True
        return False
    
    def devolver(self): #Devuelve el auto al concesionario
        self.rentado == False
        
    def __str__(self):
        return f'Auto marca {self.marca}, modelo {self.modelo}, año {self.año}.'
    
class Encargado: #Creamos el objeto encargado
    def __init__(self, nombre):
        self.nombre = nombre
         
    def acciones_encargado(self, auto, accion): #Definimos las acciones del objeto
        if accion == 'rentar':
            return auto.rentar() 
        elif accion == 'devolver':
            auto.devolver()
    
    
class Usuario: #Creamos la clase usuario
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_rentados = []
    
    def rentar_auto(self, auto, encargado): #Definimos el método rentar auto
        
        if encargado.acciones_encargado(auto, 'rentar'):
            self.carros_rentados.append(auto)
            print(f'{self.nombre} ha pedido prestado el auto {auto.marca}')
        else:
            print(f'El auto {self.marca} no está disponible.')
        
    def devolver_auto(self, auto, encargado): #Definimos el método devolver auto
        
        if auto in self.carros_rentados:
            encargado.acciones_encargado(auto, 'devolver')
            self.carros_rentados.remove(auto)
            print(f"{self.nombre} ha devuelto el auto: {auto.marca}")
        else:
            print(f"{self.nombre} no tiene el libro: {auto.marca}")
            

# Ejemplo de uso
auto = Auto('Mitsubishi', "Evo", 2003)
encargado = Encargado("Juan")
usuario = Usuario("José")

print(auto)         
usuario.rentar_auto(auto, encargado) 
usuario.devolver_auto(auto, encargado)  
        
