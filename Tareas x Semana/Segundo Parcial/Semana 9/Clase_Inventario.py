
from Clase_Producto import Producto


class Inventario:
    def __init__(self):
        self.productos = []

    #Creamos un método para mostrar el inventario
    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

    #Creamos un método para añadir un producto
    def añadir_producto(self, id, nombre, cantidad, precio):
        variable_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(variable_producto)

    #Creamos un método para eliminar un producto por el id
    def eliminar_producto_id(self):

        registro_id = input('Ingrese el ID del producto que desea eliminar: ').strip()

        for producto in self.productos:
            if producto.id == registro_id:
                self.productos.remove(producto)
                return
        print('El id no es correcto')

    #Método para actualizar el precio por ID
    def actualizar_precio(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar el precio: ').strip()
        nuevo_precio = float(input('Ingrese el nuevo precio del producto: '))

        for producto in self.productos:
            if producto.id == registro_id:
                producto.precio = nuevo_precio
                return

    #Método para actualizar la cnatidad por ID
    def actualizar_cantidad(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar: ').strip()
        nueva_cantidad = int(input('Ingrese la nueva cantidad del producto: '))

        for producto in self.productos:
            if producto.id == registro_id:
                producto.cantidad = nueva_cantidad
                return

    #Método para buscar un producto por el nombre
    def buscar_producto(self):

        nombre_producto = input('Ingrese el nombre del producto que desea buscar: ').strip()
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                print(f'El producto que estas buscando es: {producto}')


