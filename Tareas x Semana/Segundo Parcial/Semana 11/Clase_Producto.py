class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    #Creamos un método getter para cada atributo
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio(self):
        return self.__precio

    #Creamos un método setter para cada atributo
    @id.setter
    def id(self, valor):
        self.__id = valor

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    #Metodo que transforma los objetos en diccionarios
    def objeto_a_diccionario(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'cantidad': self.__cantidad,
            'precio': self.__precio
        }

    #Crea un objeto desde un diccionario
    @staticmethod
    def desde_diccionario(data):
        return Producto(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${round(self.__precio,2)}"


