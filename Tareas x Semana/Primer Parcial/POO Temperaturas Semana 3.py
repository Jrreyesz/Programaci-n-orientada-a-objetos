class SemanaTempXDia():
    def __init__(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        self.__lunes = lunes
        self.__martes = martes
        self.__miercoles = miercoles
        self.__jueves = jueves
        self.__viernes = viernes
        self.__sabado = sabado
        self.__domingo = domingo

    def promedio(self):
        prom = (self.__lunes + self.__martes + self.__miercoles + self.__jueves + self.__viernes + self.__sabado + self.__domingo)/7
        print(f'El promedio de temperatura de la semana es de: {round(prom,2)} grados.')
    
semana = SemanaTempXDia(30, 25, 30, 33, 26, 27, 28) 
semana.promedio()   



        

        
        
