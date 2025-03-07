
class Libro:
    def __init__(self, titulo, autor, categoria, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ISBN = ISBN

    def __str__(self):
        return f' Título: {self.titulo} | Autor: {self.autor} | Categoria: {self.categoria} | ISBN: {self.ISBN}'

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f' Nombre: {self.nombre} | ID: {self.id_usuario}'