class Vuelo:
    #Creamos el constructor y definimos los atributos
    def __init__(self, vuelo_numero, capacidad_pasajeros, reservados):
        self.vuelo_numero = vuelo_numero
        self.capacidad_pasajeros = capacidad_pasajeros
        self.reservados = reservados

    #Creamos un método para reservar asientos
    def reservar_asiento(self):
        if self.reservados != self.capacidad_pasajeros:
            self.reservados += 1
            print('El asiento ha sido reservado.')
        else:
            print('No hay asientos disponibles.')

    #Creamos un método para cancelar reservas
    def cancelar_reserva(self):
        if self.reservados != 0:
            self.reservados -= 1
            print('Su reserva fue cancelada.')
        else:
            print('No hay asientos reservados.')

    #Creamos un método para imprimir la informacion del vuelo
    def informacion_vuelo(self):
        print('Número de vuelo: ', self.vuelo_numero)
        print('Capacidad de pasajeros: ', self.capacidad_pasajeros)
        print('Reservados: ', self.reservados)
        print('Asientos dsiponibles: ', self.capacidad_pasajeros - self.reservados)

    #Creamos un destructor
    def __del__(self):
        print(f'El vuelo {self.vuelo_numero} ha sido eliminado.')

vuelo1 = Vuelo('M2006', 186, 180) #Creamos el objeto

vuelo1.reservar_asiento() #Reservamos un asiento
vuelo1.reservar_asiento()
vuelo1.reservar_asiento()
vuelo1.reservar_asiento()
vuelo1.reservar_asiento()
vuelo1.reservar_asiento()
vuelo1.reservar_asiento()
vuelo1.cancelar_reserva() #Cancelamos una reserva
vuelo1.reservar_asiento()
vuelo1.informacion_vuelo() #Imprimimos la información del vuelo

del vuelo1 #Utilizamos el destructor y eliminamos el objeto



