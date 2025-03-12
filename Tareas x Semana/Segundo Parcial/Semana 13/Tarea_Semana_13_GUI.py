import tkinter as tk

app = tk.Tk()
entrada = tk.StringVar(app) #Capturamos el texto que se ingresa

app.geometry('600x600') #Dimensionamos la ventana
app.configure(background='bisque3') #Colocamos un color de fondo
tk.Wm.wm_title(app, 'Crea tu lista de compras') #Título de la ventana

imagen = tk.PhotoImage(file='carrito-de-supermercado (1).png') #Una imagen que se añadirá posteriormente


lista_de_productos = [] #Aqui almacenaremos la lista de productos

frame_lista = tk.Frame(app, background='bisque3') #Creamos un frace un fondo de cierto color
frame_lista.place(x=30, y=320) #Colocamos el frame en la posición que queremos

#Creamos una función que actualice la lista dentro de la GUI
def actualizar_lista():
    for widget in frame_lista.winfo_children(): #Eliminamos duplicados
        widget.destroy()

    for i, producto in enumerate(lista_de_productos): #Creamos un bucle para recorrer los productos de la lista
        tk.Label(frame_lista, text=producto, fg='black', bg='white', width=20, anchor='w').grid(row=i, column=0) #Crearemos las etiquetas con el nombre de cada producto

        tk.Button(frame_lista,text = 'Eliminar', fg = 'white', bg = 'red', command = lambda p=producto: eliminar_producto(p)).grid(row=i, column=1) #Al mismo tiempo creamos un boton a su lado para eliminarlo

#Creamos una función añadir producto
def añadir_producto():
    producto = entrada.get().strip() #Elimina espacios innecesarios y capta el texto
    if producto: #Comprueba si existe texto en la entrada
        lista_de_productos.append(producto) #Añade el producto a la lista
        print(lista_de_productos)
        entrada.set('') #Deja vacio otra vez el cuadro de texto
        actualizar_lista() #LLama a la función actualizar la lista

#Función para eliminar un producto
def eliminar_producto(producto):
    if producto in lista_de_productos: #Verifica que el producto esta en la lista
        lista_de_productos.remove(producto) #Lo elimina
        actualizar_lista() #Llama a la función actualizar lista


tk.Button(
    app,
    text = 'Añadir',
    font = ('Times New Roman', 14),
    bg = 'LightSkyBlue3',
    fg = 'white',
    command = añadir_producto
).place(
    x=275,
    y=250
)

etiqueta_imagen = tk.Label(app, image=imagen)
etiqueta_imagen.place(x=245,y=30)

tk.Label(
    app,
    text='Introduce un producto',
    fg='white',
    bg='LightGoldenrod4',
    justify='center'
).place(
    x=250,
    y=195
)

tk.Label(
    app,
    text='Lista de Productos',
    fg='black',
    bg='white',
    justify='center',
).place(
    x = 30,
    y = 300
)

tk.Entry(
    fg = 'black',
    bg = 'LightGoldenrod3',
    justify = 'center',
    textvariable = entrada
).place(
    x=250,
    y=220
)



app.mainloop()