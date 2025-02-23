
from Clase_Producto import Producto

producto1 = Producto(1, 'Manzanas', 23, 0.26)
producto2 = Producto(2, 'Peras', 33, 0.27)
producto3 = Producto(3, 'Uvas', 25, 1.5)
producto4 = Producto(4, 'Duraznos', 50, 0.35)
producto5 = Producto(5, 'Cerezas', 20, 1.30)

class Inventario:
    def __init__(self):
        self.productos = [producto1, producto2, producto3, producto4, producto5]

    #Creamos un método para mostrar el inventario
    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

    #Creamos un método para añadir un producto
    def añadir_producto(self, id, nombre, cantidad, precio):
        variable_producto = Producto(id, nombre, cantidad, precio)
        for producto in self.productos:
            if producto.id == variable_producto.id:
                print('El id escrito ya esta en uso.')
                break
            elif producto.id != variable_producto.id:
                self.productos.append(variable_producto)
                print(f'El producto {variable_producto} fue añadido correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nEl producto {variable_producto} fue añadido correctamente.')
                except Exception as error:
                    print('El producto no se añadió correctamente al archivo inventario:', error)
                else:
                    print('El producto fue añadido correctamente al archivo inventario.')



    #Creamos un método para eliminar un producto por el id
    def eliminar_producto_id(self):

        registro_id = input('Ingrese el ID del producto que desea eliminar: ').strip()

        for producto in self.productos:
            if producto.id == registro_id:
                self.productos.remove(producto)
                print(f'El producto {producto.nombre} fue eliminado correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nEl producto {producto.nombre} fue eliminado correctamente.')
                except Exception as error:
                    print('El producto eliminado no se añadió correctamente al archivo inventario:', error)
                else:
                    print('La eliminación del producto fue añadida correctamente al archivo inventario.')
            else:
                print('El id no es correcto')



    #Método para actualizar el precio por ID
    def actualizar_precio(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar el precio: ').strip()
        nuevo_precio = float(input('Ingrese el nuevo precio del producto: '))

        for producto in self.productos:
            if producto.id == registro_id:
                producto.precio = nuevo_precio
                print(f'El precio del producto {producto.nombre} fue modificado correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nEl precio del producto {producto.nombre} fue modificado correctamente.')
                except Exception as error:
                    print(f'La modificación del producto {producto.nombre }no se añadió correctamente al archivo inventario:', error)
                else:
                    print(f'La modificación del producto {producto.nombre}fue añadida correctamente al archivo inventario.')


    #Método para actualizar la cnatidad por ID
    def actualizar_cantidad(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar: ').strip()
        nueva_cantidad = int(input('Ingrese la nueva cantidad del producto: '))

        for producto in self.productos:
            if producto.id == registro_id:
                producto.cantidad = nueva_cantidad
                print(f'La cantidad del producto {producto.nombre} fue modificada correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nLa cantidad del producto {producto.nombre} fue modificada correctamente.')
                except Exception as error:
                    print(f'La modificación del producto {producto.nombre} no se añadió correctamente al archivo inventario:', error)
                else:
                    print(f'La modificación del producto {producto.nombre} fue añadida correctamente al archivo inventario.')


    #Método para buscar un producto por el nombre
    def buscar_producto(self):

        nombre_producto = input('Ingrese el nombre del producto que desea buscar: ').strip()
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                print(f'El producto que estas buscando es: {producto}')


