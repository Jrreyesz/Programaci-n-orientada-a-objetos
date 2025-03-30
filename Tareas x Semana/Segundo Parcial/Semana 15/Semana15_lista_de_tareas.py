#Importar las librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Creames el objeto de la aplicación
class AplicacionListaTareas:
    def __init__(self, ventana):
        #Definimos sus atributos
        self.ventana = ventana
        self.ventana.title('Lista de Tareas')
        self.ventana.geometry('1000x600')

        #Almacenamos la entrada del campo de texto tarea
        self.entrada_tarea = tk.StringVar(ventana)

        #Creamos un frame para almacenar los campos de entrada
        self.frame = tk.Frame(self.ventana, width=320, height=300)
        self.frame.config(bg='LightCyan3')
        self.frame.place(x = 10, y = 10)

        #Creamos un label para el campo de entrada
        self.label_tarea = tk.Label(self.frame, text='Escriba la tarea que desea guardar', width = 40)
        self.label_tarea.config(bg='LightCyan1')
        self.label_tarea.place(x = 18, y = 10)

        #Creamos el campo de entrada de texto
        self.tarea = tk.Entry(self.frame, width = 46, textvariable = self.entrada_tarea)
        self.tarea.config(bg='LightBlue1')
        self.tarea.place(x = 20, y = 40)

        #Creamos un boton para ingresar tarea y lo asociamos a su evento
        self.btn_ingresar_tarea = tk.Button(self.frame, text = 'Añadir Tarea')
        self.btn_ingresar_tarea.config(bg='light cyan', command = self.actualizar_lista)
        self.btn_ingresar_tarea.place(x = 130, y = 70)

        #Creamos un boton para marcar tarea y lo asociamos a su evento
        self.btn_marcar_completada = tk.Button(self.ventana, text = 'Marcar Tarea Completada')
        self.btn_marcar_completada.config(bg='DodgerBlue4', fg = 'white', command = self.marcar_tarea_completada)
        self.btn_marcar_completada.place(x = 350, y = 250)

        #Creamos un boton para eliminar tarea y lo asociamos a su evento
        self.btn_eliminar_tarea = tk.Button(self.ventana, text = 'Eliminar Tarea')
        self.btn_eliminar_tarea.config(bg = 'red', fg = 'white', command = self.eliminar_tarea)
        self.btn_eliminar_tarea.place(x = 869, y = 250)

        #Estilo para ponerle fondo a los headings
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Treeview.Heading', background='chartreuse4', foreground='white')

        #Estilo para las filas del Treeview
        self.style2 = ttk.Style()
        self.style2.configure("Custom.Treeview", background="white")
        self.style2.map("Custom.Treeview", background=[("selected", "#add8e6")])

        #Creamos un Treeview
        self.tv = ttk.Treeview(self.ventana)
        self.tv.tag_configure("colored", background="yellow")

        self.tv.column('#0', width=600)

        self.tv.heading('#0', text='Tarea(s)')

        self.tv.place(x = 350, y = 10)

        #Asociamos el evento de aplastar la tecla enter a la función de actualizar lista
        self.ventana.bind('<Return>', self.actualizar_lista)

    #Creamos la funcion para actualizar lista
    def actualizar_lista(self, evento = 'none'):
        #Verificamos que haya algo en el campo de entrada
        if self.entrada_tarea.get():
            #Ingresamos una fila con los datos ingresados
            self.tv.insert('', tk.END, text = self.entrada_tarea.get())
            #Limpiamos el campo de texto
            self.entrada_tarea.set('')

    #Funcion que marcara de un color distinto las tareas completadas
    def marcar_tarea_completada(self):
        #Almacenamos el item seleccionado
        seleccion = self.tv.selection()
        #Verificamos que este seleccionado algo
        if seleccion:
            #Si es así, cambiamos el color de la fila seleccionada
            self.tv.item(seleccion, tags = ('colored',))
        else:
            #Caso contrario enviar un mensaje de error
            messagebox.showinfo('Error', 'No hay tareas seleccionadas')

    #Función para eliminar tarea
    def eliminar_tarea(self):
        seleccion = self.tv.selection()
        if seleccion:
            #Eliminamos la fila selccionada
            self.tv.delete(seleccion)
        else:
            #De lo contrario eviamos un mensaje de error
            messagebox.showinfo(message = 'Tarea no seleccionada', title = 'Error')

#Creamos la ventana
ventana = tk.Tk()
#Creamos el objeto
aplicacion = AplicacionListaTareas(ventana)

ventana.mainloop()