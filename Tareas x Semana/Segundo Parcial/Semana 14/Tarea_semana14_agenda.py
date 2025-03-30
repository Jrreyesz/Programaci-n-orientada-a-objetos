#Importamos las librerias que vamos a necesitar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

#Creamos la ventana principal
ventana = tk.Tk()
ventana.geometry('1000x600')
ventana.title('Agenda Personal')

#Creamos un TreeView en forma de tabla
tv = ttk.Treeview(ventana, columns = ('Hora', 'Descripción'))
#Creamos sus columnas

tv.column('Hora', width=150, anchor = tk.CENTER)
tv.column('Descripción', width=150, anchor = tk.CENTER)

#Colocamos un título a cada columna
tv.heading('#0', text='Fecha', anchor=tk.CENTER)
tv.heading('Hora', text='Hora', anchor=tk.CENTER)
tv.heading('Descripción', text = 'Descripción', anchor = tk.CENTER)

#Ubicamos el TreeView dentro de la ventana
tv.place(x = 350, y = 10)

#Estas variables almacenaran los datos ingresados en las respectivas entradas
variable_calendario = tk.StringVar(ventana)
variable_hora = tk.StringVar(ventana)
variable_descripcion = tk.StringVar(ventana)

#Con esta función actualizamos la agenda
def actualizar_agenda():
    #Verificamos que todos los datos esten ingresados
    if variable_calendario.get():
        if variable_hora.get():
            if variable_descripcion.get():
                #Insertamos una fila con los datos correspondientes a cada columna
                tv.insert('', tk.END, text = variable_calendario.get(), values = (variable_hora.get(), variable_descripcion.get()))
                #Vaciamos los campos de entrada para que se puedan ingresar nuevos datos
                variable_calendario.set('')
                variable_hora.set('')
                variable_descripcion.set('')
                #Eviamos un mensaje de diálogo que indica que se agregó con éxito el evento
                messagebox.showinfo(message = 'Evento agregado con éxito.')

#Función para eliminar un evento seleccionado
def eliminar_evento():
    #Con el try nos aseguramos que haya elegido un evento para eliminar, de lo contrario se le notificara
    try:
        #Obtenemos la selección del evento del usuario
        item_seleccionado = tv.selection()[0]
        #Eliminamos el evento
        tv.delete(item_seleccionado)
    except:
        messagebox.showinfo(message = 'Primero seleccione el elemento que desea eliminar.', title = 'Error')

#Función para salir por completo de la ventana
def salir():
    ventana.quit()

#Creamos un frame para introducir los datos
frame_datos= tk.Frame(ventana)
frame_datos.configure(width = 300, height = 580, bg = 'bisque2')
frame_datos.place(x = 10, y = 10)

#Etiqueta correspondiente a la entrada calendario
label_calendario = tk.Label(frame_datos, text='Elija una fecha')
label_calendario.config(width = 30, bg = 'goldenrod')
label_calendario.place(x = 40, y = 20)

#Ubicamos la entrada de la fecha con la libreria tkcalendar
calendario = DateEntry(frame_datos, width = 32, textvariable = variable_calendario)
calendario.place(x = 40, y = 50)

#Etiqueta correspondiente a la entrada hora
label_hora = tk.Label(frame_datos, text='Escriba la hora')
label_hora.config(width = 30, bg = 'goldenrod')
label_hora.place(x = 40, y = 80)

#Creamos la entrada de texto para la hora
entrada_hora = tk.Entry(frame_datos, width = 35, textvariable = variable_hora)
entrada_hora.place(x = 40, y = 110)

#Etiqueta correspondiente a la entrada descripcion
label_descripcicion = tk.Label(frame_datos, text='Escriba una descripción')
label_descripcicion.config(width = 30, bg = 'goldenrod')
label_descripcicion.place(x = 40, y = 140)

#Creamos la entrada de texto para la descripcion
entrada_descripcion = tk.Entry(frame_datos, width = 35, textvariable = variable_descripcion)
entrada_descripcion.place(x = 40, y = 170)

#Creamos el botón agregar y lo vinculamos con su respectiva funcion
boton_agregar = tk.Button(frame_datos, text = 'Agregar')
boton_agregar.config(width = 40, bg = 'SkyBlue3', command = actualizar_agenda)
boton_agregar.place(x = 4, y = 550)

#Creamos el botón eliminar y lo vinculamos con su respectiva funcion
boton_eliminar = tk.Button(ventana, text = 'Eliminar evento')
boton_eliminar.config(width = 20, bg = 'SkyBlue3', command = eliminar_evento)
boton_eliminar.place(x = 350, y = 250)

#Creamos el botón salir y lo vinculamos con su respectiva funcion
boton_salir = tk.Button(ventana, text = 'Salir', fg = 'white')
boton_salir.config(width = 20, bg = 'red', command = salir)
boton_salir.place(x = 830, y = 570)



ventana.mainloop()