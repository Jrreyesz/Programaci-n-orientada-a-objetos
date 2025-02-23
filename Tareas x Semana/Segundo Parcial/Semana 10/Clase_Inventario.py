
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

    #Creamos un metodo para almacenar todos los ids de los productos del inventario
    def todos_los_id(self):
        self.lista_de_ids = []
        for i in range(len(self.productos)):
            self.lista_de_ids.append(int(self.productos[i].id))


    #Creamos un método para añadir un producto
    def añadir_producto(self, id, nombre, cantidad, precio):

        variable_producto = Producto(id, nombre, cantidad, precio)

        #Llamamos al metodo todos_los_id para que se cree la lista con todos los ids existentes en el invenario
        self.todos_los_id()

        #Comprobamos que el id del nuevo producto no se encuentre dentro de los ids existentes
        if int(variable_producto.id) in self.lista_de_ids:
            print('El id escrito ya esta en uso. Intente otra vez.')
        else:
            self.productos.append(variable_producto)
            print(f'El producto {variable_producto} fue añadido correctamente.')

            #Manejamos los errores que se puedan dar al crear el archivo
            try:
                #Utilizamos 'a' para que no se borre el archivo y no se sobreescriba todo desde cero
                with open('inventario.txt', 'a') as archivo:
                    archivo.write(f'\nEl producto {variable_producto} fue añadido correctamente.')
            except Exception as error:
                print('El producto no se añadió correctamente al archivo inventario:', error)
            #Este else sirve para que se nos notifique si no hubo una excepción en el programa
            else:
                print('El producto fue añadido correctamente al archivo inventario.')



    #Creamos un método para eliminar un producto por el id
    def eliminar_producto_id(self):

        registro_id = input('Ingrese el ID del producto que desea eliminar: ').strip()

        for producto in self.productos:
            if str(producto.id) == registro_id:
                self.productos.remove(producto)
                print(f'El producto {producto.nombre} fue eliminado correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nEl producto {producto.nombre} fue eliminado correctamente.')
                except Exception as error:
                    print('El producto eliminado no se añadió correctamente al archivo inventario:', error)
                else:
                    print('La eliminación del producto fue añadida correctamente al archivo inventario.')
                return
        print('El id ingresado no es correcto.')



    #Método para actualizar el precio por ID
    def actualizar_precio(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar el precio: ').strip()


        for producto in self.productos:
            if str(producto.id) == registro_id:
                nuevo_precio = float(input('Ingrese el nuevo precio del producto: '))
                producto.precio = nuevo_precio
                print(f'El precio del producto {producto.nombre} fue modificado correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nEl precio del producto {producto.nombre} fue modificado correctamente.')
                except Exception as error:
                    print(f'La modificación del producto {producto.nombre }no se añadió correctamente al archivo inventario:', error)
                else:
                    print(f'La modificación del producto {producto.nombre}fue añadida correctamente al archivo inventario.')
                return
        print('El id ingresado no es correcto.')

    #Método para actualizar la cnatidad por ID
    def actualizar_cantidad(self):

        registro_id = input('Ingrese el ID del producto al que le desea modificar: ').strip()


        for producto in self.productos:
            if str(producto.id) == registro_id:
                nueva_cantidad = int(input('Ingrese la nueva cantidad del producto: '))
                producto.cantidad = nueva_cantidad
                print(f'La cantidad del producto {producto.nombre} fue modificada correctamente.')
                try:
                    with open('inventario.txt', 'a') as archivo:
                        archivo.write(f'\nLa cantidad del producto {producto.nombre} fue modificada correctamente.')
                except Exception as error:
                    print(f'La modificación del producto {producto.nombre} no se añadió correctamente al archivo inventario:', error)
                else:
                    print(f'La modificación del producto {producto.nombre} fue añadida correctamente al archivo inventario.')
                return
        print('El id ingresado no es correcto.')

    #Método para buscar un producto por el nombre
    def buscar_producto(self):

        nombre_producto = input('Ingrese el nombre del producto que desea buscar: ').strip()
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                print(f'El producto que estas buscando es: {producto}')
                return
        print('Producto no encontrado.')


