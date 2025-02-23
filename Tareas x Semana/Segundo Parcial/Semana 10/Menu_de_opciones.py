from unicodedata import category

from Clase_Inventario import Inventario

inventario = Inventario()



while True:

    print('\n1. Eliminar producto')
    print('2. Actualizar precio')
    print('3. Actualizar cantidad')
    print('4. Buscar producto')
    print('5. Mostrar inventario')
    print('6. Añadir producto')
    print('7. Salir del programa')

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
        id = input('Ingrese el id del producto: ')
        nombre = input('Ingrese el nombre del producto: ')
        cantidad = int(input('Ingrese el cantidad del producto: '))
        precio = float(input('Ingrese el precio del producto: '))
        inventario.añadir_producto(id, nombre, cantidad, precio)
        print('Cambio hecho satisfactoriamente.')
    elif opcion == '7':
        print('Ha salido del programa')
        break
    else:
        print('Opción no valida, ingrese una nueva. ')
