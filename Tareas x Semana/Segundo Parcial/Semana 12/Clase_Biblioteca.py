import pickle

from Clase_Libro_y_Clase_Usuario import Libro
from Clase_Libro_y_Clase_Usuario import Usuario

usuario1 = Usuario('Pedro', '1')
usuario2 = Usuario('Juan', '2')
usuario3 = Usuario('Maria', '3')

libro1 = Libro('El mejor libro del mundo', 'Manuel Vilas', 'No ficcion', '978-628-7579-78-1')
libro2 = Libro('Los besos', 'Manuel Vilas', 'Contemporanea', '978-958-42-9676-4')
libro3 = Libro('Los fantasmas de una vida', 'Hilary Mantel', 'No ficcion', '978-628-7579-29-3')
libro4 = Libro('El jardín de las mariposas', 'Dot Hutchison', 'Literaria', '978-628-7574-95-3')

class Biblioteca:
    def __init__(self):

        datos = self.cargar_datos() #Sirve para cargar los datos del programa

        if datos: #Condicion para ver si hay datos que retomar
            self.libros_disponibles, self.usuarios = datos
        else: #Si no los hay toma los que estan por defecto
            self.libros_disponibles = dict({
                libro1.ISBN : libro1,
                libro2.ISBN : libro2,
                libro3.ISBN : libro3,
                libro4.ISBN : libro4
            })
            self.usuarios = [usuario1, usuario2, usuario3]

    def guardar_datos(self): #Metodo para guardar los datos
        with open("biblioteca.pkl", "wb") as archivo:
            pickle.dump((self.libros_disponibles, self.usuarios), archivo)
        print("Datos guardados correctamente.")

    #Metodo para cargar los datos
    def cargar_datos(self):

        try:
            with open("biblioteca.pkl", "rb") as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return None


    def añadir_libro(self, titulo, autor, categoria, ISBN):

        variable_libro = Libro(titulo, autor, categoria, ISBN) #Pedir al usuario los datos del objeto

        for key in self.libros_disponibles.keys(): #Recorro con el bucle las claves del diccionario que son los ISBN
            if key == variable_libro.ISBN: #Comparo los ISBN Para ver si el libro que quiero añadir esta disponible
                print('El libro ya se encuentra disponible.')
                return

        self.libros_disponibles[variable_libro.ISBN] = variable_libro #SI el libro no existe lo añadimos
        self.guardar_datos()
        print('Libro agregado con éxito.')

    def quitar_libro(self):

        isbn = input('Ingrese el ISBN del libro que desea eliminar: ')

        clave_a_eliminar = [clave for clave, libro in self.libros_disponibles.items() if libro.ISBN == isbn] #Almacenar la clave que vamos a eliminar, el libro

        if not clave_a_eliminar: #Condicion para ver si se encontró una clave coincidente
            print('No se logró encontrar el libro.')
            return

        for clave in clave_a_eliminar: #Eliminamos al objeto a través de su clave
            del self.libros_disponibles[clave]
            self.guardar_datos()

        print(f"El libro ha sido eliminado.")

    def registrar_usuario(self, nombre, id):

        variable_usuario = Usuario(nombre, id) #Pedimos que se ingresen por teclado los datos del usuario

        for usuario in self.usuarios: #Verificamos que el usuario exista
            if usuario.id_usuario == variable_usuario.id_usuario:
                print('El id de usuario ya existe.')
                return

        self.usuarios.append(variable_usuario) #Si no existe se agrega a la lista de objetos usuarios
        self.guardar_datos()
        print('Usuario ingresado correctamente.')

    def dar_de_baja_usuario(self):

        id = int(input('Ingrese el ID del usuario que desea eliminar: '))

        if self.usuarios: #Verificamos que existan usuarios
            for usuario in self.usuarios:
                if str(usuario.id_usuario) == str(id): #Si existen usuarios recorremos el id de cada usuario para encontrar coincidencias
                    print(f'El usuario {usuario} ha sido eliminado.')
                    self.usuarios.remove(usuario)
                    self.guardar_datos()
                    return
            print('El usuario no existe.')

        else:
            print('No hay usuarios disponibles.')

    def prestar_libro(self):

        id = int(input('Ingrese el id del usuario que desea el libro: '))
        isbn = input('Ingrese el ISBN del libro que desea prestar: ')

        for usuario in self.usuarios: #Recorremos todos los usuarios
            if usuario.id_usuario == str(id): #Verificamos que el id del usuario exista
                for key,value in self.libros_disponibles.items(): #Desempaquetamos las claves y valores del diccionario donde estan los libros
                    if key == isbn: #SI el ISBN del objeto del diccionario coincide con el ISBN buscado
                        usuario.libros_prestados.append(value) #Si hay coincidencia, se añade a la lista de libros prestados
                        self.libros_disponibles.pop(key) #Eliminamos el libro de los disponibles
                        self.guardar_datos()
                        print(f'El libro fue prestado correctamente a {usuario.nombre}')
                        return
                print('El ISBN no existe.')
                return
        print('El usuario no existe.')

    def devolver_libro(self):

        id = int(input('Ingrese el id del usuario que desea regresar el libro: '))
        isbn = input('Ingrese el ISBN del libro que desea regresar: ')

        for usuario in self.usuarios: #Recorremos todos los usuarios
            if usuario.id_usuario == str(id): #verificamos que exista el usuario
                for libro in usuario.libros_prestados: #Verificamos la lista de libros prestados
                    if isbn == libro.ISBN: #Buscamos que coincida el ISBN para eliminar el libro
                        self.libros_disponibles[libro.ISBN] = libro #Devolvemos el libro a los libros disponibles
                        usuario.libros_prestados.remove(libro) #Eliminamos el libro de los libros prestados
                        self.guardar_datos()
                        print(f'El usuario {usuario.nombre} ha regresado el libro correctamente.')
                        return
                print('El ISBN no existe o no esta disponible.')
                return
        print('El usuario no existe.')

    def buscar_libro(self):

        eleccion_ususario = input('¿Desea buscar el libro por título, autor o categoría? ')

        #Usamos una condición para que el usuario elija que opción de búsqueda desea

        if eleccion_ususario.lower() == 'titulo':

            libro_a_buscar = input('Ingrese el título del libro que desea buscar: ')

            for libro in self.libros_disponibles.values(): #Tomamos el objeto de cada elemento del diccionario
                if libro.titulo.lower() == libro_a_buscar.lower(): #Buscamos coincidencia con el respectivo parámetro de búsqueda
                    print(f'El libro que estas buscando es {libro}')
                    return
            print('El libro no se encuentra disponible, o su búsqueda esta mal escrita.')

        elif eleccion_ususario.lower() == 'autor':

            libros_encontrados = [] #Como puede haber más de un elemento creamos una lista que los almacene

            libro_a_buscar = input('Ingrese el autor del libro que desea buscar: ')

            for libro in self.libros_disponibles.values(): #Recorrimos los objetos del diccionario
                if libro.autor.lower() == libro_a_buscar.lower():
                    libros_encontrados.append(libro) #Si hay coincidencias añadimos el libro a la lista de libros encontrados

            if libros_encontrados: #imprime en pantalla las coincidencias encontradas
                print('Los libros del autor son: ')
                for libro in libros_encontrados:
                    print(f'{libro}')
            else:
                print('No se encontraron libros del autor o no estan disponibles en este momento.')

        #Repetimos el proceso seguido anteriormente
        elif eleccion_ususario.lower() == 'categoria':

            libros_encontrados = []

            libro_a_buscar = input('Ingrese la categoría del libro que desea buscar: ')

            for libro in self.libros_disponibles.values():
                if libro.categoria.lower() == libro_a_buscar.lower():
                    libros_encontrados.append(libro)

            if libros_encontrados:
                print('Los libros de la categoria son: ')
                for libro in libros_encontrados:
                    print(f'{libro}')
            else:
                print('No se encontraron libros en la categoria o no estan disponibles en este momento.')

    def lista_de_libros_prestados(self):

        id = input('Ingrese el id del usuario al que le desea ver los libros prestados: ')

        for usuario in self.usuarios: #Recorremos todos los usuarios
            if usuario.id_usuario == id: #Buscamos coincidencia con el id de usuario que estamos buscando
                if usuario.libros_prestados: #Condición para verificar que existan libros prestados en el usuario
                    print('El usuario tiene los siguientes libros prestados: ')
                    for libro in usuario.libros_prestados: #Bucle para imprimir todos los libros encontrados en el usuario
                        print(f'{libro}')
                else:
                    print('El usuario no tiene libros prestados.')
                return
        print('ID del usuario no encontrado')

















