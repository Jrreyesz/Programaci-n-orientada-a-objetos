#Importamos las librerias necesarias
import tkinter as tk
from tkinter import ttk

#Creamos la clase de la app
class AppListaTareas:
    #Definimos sus atributos
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Lista de tareas pendientes')
        self.ventana.geometry('1000x600')
        self.ventana.config(bg='SteelBlue4')

        #Alacenamos lo que se escribe en la entrada de tarea
        self.variable_tarea = tk.StringVar()

        # Estilo para ponerle fondo a los headings
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Treeview.Heading', background='DarkGoldenrod3', foreground='white')

        # Estilo para las filas del Treeview
        self.style2 = ttk.Style()
        self.style2.configure("Custom.Treeview", background="white")
        self.style2.map("Custom.Treeview", background=[("selected", "#add8e6")])

        #Creamos el treeview
        self.tv = ttk.Treeview(self.ventana)
        self.tv.tag_configure("colored", background="yellow")
        self.tv.column('#0', width = 770, anchor = tk.CENTER)
        self.tv.heading('#0', text='Tareas', anchor = tk.CENTER)
        self.tv.place(x = 20, y = 20)

        #Creamos el boton eliminar, lo asociamos a su evento, pero no lo hacemos visible
        self.btn_eliminar = tk.Button(self.ventana, text='Eliminar', background='red4', fg='white', width=9, command = self.eliminar_tarea)
        self.btn_eliminar.place_forget()

        #Creamos el boton marcar, lo asociamos a su evento, pero no lo hacemos visible
        self.btn_marcar = tk.Button(self.ventana, text='Marcar como hecha', background='green4', fg='white', command = self.marcar_tarea_completada)
        self.btn_marcar.place_forget()

        #Creamos el campo de entrada a tarea
        self.entry_tarea = tk.Entry(self.ventana, textvariable = self.variable_tarea, foreground='black')
        self.entry_tarea.config(width = 100)
        self.entry_tarea.place(x = 20, y = 260)

        #Creamos un boton agregar tareea y le asociamos un evento
        self.btn_agragar_tarea = tk.Button(self.ventana, text = 'Añadir tarea', command = self.actualizar_agenda)
        self.btn_agragar_tarea.config(width = 20, bg = 'DeepSkyBlue3')
        self.btn_agragar_tarea.place(x = 645, y = 255)

        #Asociamos un evento para que se muestren los botones bajo una condición
        self.tv.bind('<<TreeviewSelect>>', self.mostrar_botones_seleccion)

        #Asociamos el evento de aplastar la tecla enter a la función de actualizar lista
        self.ventana.bind('<Return>', self.actualizar_agenda)

        #Asociamos el evento de tecla a la función
        self.ventana.bind('c', self.marcar_tarea_completada)
        self.ventana.bind('C', self.marcar_tarea_completada)

        # Asociamos el evento de tecla a la función
        self.ventana.bind('d', self.eliminar_tarea)
        self.ventana.bind('D', self.eliminar_tarea)

        # Asociamos la tecla 'Escape' para cerrar la aplicación
        self.ventana.bind('<Escape>', self.cerrar_aplicacion)

    #Creamos una función para actualizart la agenda
    def actualizar_agenda(self, event = None):
        #Verificamos que haya algo en el campo de entrada
        if self.variable_tarea.get():
            #Si lo hay se agrega la tarea y se deja el campo en blanco otra vez
            self.tv.insert('', tk.END, text = self.variable_tarea.get())
            self.variable_tarea.set('')

    #Creamos un metodo para mostrar los botones
    def mostrar_botones_seleccion(self, event = None):
        seleccion = self.tv.selection()
        #Verificamos que alguna tarea este seleccionada
        if seleccion:
            #Si la condicion se cumple, se mostraran los botones
            self.btn_eliminar.place(x=800, y=20)
            self.btn_marcar.place(x=880, y=20)
        else:
            # Si no hay ninguna fila seleccionada, ocultamos los botones
            self.btn_eliminar.place_forget()
            self.btn_marcar.place_forget()

    #Creamos una funcion para eliminar tareas
    def eliminar_tarea(self, event = None):
        seleccion = self.tv.selection()
        #Verificamos que exista una fila seleccionada
        if seleccion:
            #Si la condicion se cumple se elimina la fila seleccionada
            self.tv.delete(seleccion)

    # Funcion que marcara de un color distinto las tareas completadas
    def marcar_tarea_completada(self, event = None):
        # Almacenamos el item seleccionado
        seleccion = self.tv.selection()
        # Verificamos que este seleccionado algo
        if seleccion:
            # Si es así, cambiamos el color de la fila seleccionada
            self.tv.item(seleccion, tags=('colored',))

    def cerrar_aplicacion(self, event = None):
        self.ventana.quit()


ventana = tk.Tk()
aplicacion = AppListaTareas(ventana)
ventana.mainloop()