lista_alumnos = []         #Creamos lista vacia para almacenar nombre de los alumnos
lista_alumnos_notas = []   #Creamos lista vacía para almacenar diccionarios con los nombres de los alumnos y sus notas

def lista_de_alumnos():    #Creamos una función para añadir una cantidad de alumnos determinada
    
    controlador = 'si'
    while controlador.lower() == 'si':
        nombre_alumno = input('Ingrese el nombre del alumno: ')
        lista_alumnos.append(nombre_alumno)
        controlador = input('¿Desea ingresar el nombre de otro alumno? ')

lista_de_alumnos() #Llamamos a la funcion para crear la lista de estudiantes

materias = ['Física', 'Química', 'Biología', 'Filosofía'] #Creamos una lista de materias
materias = dict.fromkeys(materias) #Transformamos esa lista en un diccionario con valores vacios

for n in range(len(lista_alumnos)): # Utilizamos bucle for para añadir los valores a las keys del diccionario
    materias = materias.fromkeys(materias) #En cada vuelta las claves se borran
    materias['Nombre'] = lista_alumnos[n] #Se añade la clave nombre y el nombre del alumno correspondiente en la lista
    for m in materias.keys(): 
        if m != 'Nombre': # Asignamos un valor a cada a clave con excepción a la clave nombre
            materias[m] = float(input(f'Ingrese la nota de {m} del alumno {lista_alumnos[n]}: '))
    lista_alumnos_notas.append(materias) #Añadimos los datos del estudiante como diccionario a una lista
    
for i in lista_alumnos_notas:
    print(i) #Se imprimen los datos de todos los alumnos con sus notas

      
        
        
            
            
            
         
      

    


        
    