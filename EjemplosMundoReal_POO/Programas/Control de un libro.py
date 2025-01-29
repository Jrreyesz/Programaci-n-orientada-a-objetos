class Libro:
    
    def __init__(self, titulo, autor, paginas, paginas_leidas): #Creamos la clase libro y las abstracciones
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_leidas = paginas_leidas
        
    def ver_detalles(self): #Creamos un método para ver los detalles del libro
        print(self.titulo, ':', sep='')
        print('Autor: ', self.autor)
        print('Páginas: ', self.paginas)
        print('Páginas leídas: ', self.paginas_leidas)
        
    def leer_paginas(self, leer): #Creamos un metodo para leer paginas
        if self.paginas_leidas + leer <= self.paginas:
            self.paginas_leidas += leer
            print(f"Has leído {leer} páginas. Páginas leídas en total: {self.paginas_leidas}")
        else:
            print('Has acabado el libro, no tienes más que leer.')
            
libro = Libro('EL Principito', 'Antoine de Saint-Exupéry', 111, 0) #Creamos un objeto

libro.ver_detalles() #Llamamos al metodo ver_detalles

libro.leer_paginas(36) #Leemos páginas
libro.leer_paginas(36)
libro.leer_paginas(39)
libro.leer_paginas(10)
            
libro.ver_detalles() #Observamos los detalles actualizados
        
        