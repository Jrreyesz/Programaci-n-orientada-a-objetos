from Clase_Libro_y_Clase_Usuario import Libro
from Clase_Libro_y_Clase_Usuario import Usuario
from Clase_Biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print('\n1. Añadir libro')
    print('2. Quitar libro')
    print('3. Registrar usuario')
    print('4. Dar de baja usuario')
    print('5. Prestar libro')
    print('6. Devolver libro')
    print('7. Buscar libro')
    print('8. Ver lista de libros prestados')
    print('9. Salir')

    opcion = input('¿Qué desea hacer? ')

    if opcion == '1':
        titulo = input('Ingrese el título del libro: ')
        autor = input('Ingrese el autor: ')
        categoria = input('Ingrese la categoria: ')
        ISBN = input('Ingrese el ISBN: ')
        biblioteca.añadir_libro(titulo, autor, categoria, ISBN)

    elif opcion == '2':
        biblioteca.quitar_libro()

    elif opcion == '3':
        nombre = input('Ingrese el nombre: ')
        id = input('Ingrese el id del usuario: ')
        biblioteca.registrar_usuario(nombre, id)

    elif opcion == '4':
        biblioteca.dar_de_baja_usuario()

    elif opcion == '5':
        biblioteca.prestar_libro()

    elif opcion == '6':
        biblioteca.devolver_libro()

    elif opcion == '7':
        biblioteca.buscar_libro()

    elif opcion == '8':
        biblioteca.lista_de_libros_prestados()

    elif opcion == '9':
        print('Ha terminado el programa exitosamente.')
        break
    else:
        print('Opción no valida, intentelo de nuevo.')

