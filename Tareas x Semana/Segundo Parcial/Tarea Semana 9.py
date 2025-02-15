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


    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${round(self.__precio,2)}"

class Inventario:
    def __init__(self):
        self.productos = []

    #Creamos un método para mostrar el inventario
    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

    #Creamos un método para añadir un producto
    def añadir_producto(self, producto):

        for p in self.productos:
            if p.id == producto.id:
                print(f"Error: Ya existe un producto con el ID '{producto.id}'.")
                return

        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

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


inventario = Inventario()

producto_1 = Producto('PRO1', 'Manzanas', 50, 0.33)
producto_2 = Producto('PRO2', 'Cloro', 25, 2.5)
producto_3 = Producto('PRO3', 'Cereal', 30, 2.75)
producto_4 = Producto('PRO4', 'Leche 1L', 30, 1.10)
producto_5 = Producto('PRO5', 'Coca Cola 1L', 20, 1.25)

inventario.añadir_producto(producto_1)
inventario.añadir_producto(producto_2)
inventario.añadir_producto(producto_3)
inventario.añadir_producto(producto_4)
inventario.añadir_producto(producto_5)


while True:

    print('\n1. Eliminar producto')
    print('2. Actualizar precio')
    print('3. Actualizar cantidad')
    print('4. Buscar producto')
    print('5. Mostrar inventario')
    print('6. Salir del programa')

    opcion = input('¿Qué desea hacer? ')

    if opcion == '1':
        inventario.eliminar_producto_id()
        print('Cambio hecho satisfactoriamente.')
    elif opcion == '2':
        inventario.actualizar_precio()
        print('Cambio hecho satisfactoriamente.')
    elif opcion == '3':
        inventario.actualizar_cantidad()
        print('Cambio hecho satisfactoriamente.')
    elif opcion == '4':
        inventario.buscar_producto()
        print('Ejecutado correctamente.')
    elif opcion == '5':
        print('Inventario: ')
        inventario.mostrar_inventario()
    elif opcion == '6':
        print('Ha salido del programa')
        break
    else:
        print('Opción no valida, ingrese una nueva. ')





