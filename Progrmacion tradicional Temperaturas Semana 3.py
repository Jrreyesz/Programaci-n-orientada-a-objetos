#Programación tradicional

matriz_temp=[]

def lista():
    for i in range(7):
        temperaturas = float(input(f'Ingrese la temperatura del {i+1} día: '))
        matriz_temp.append(temperaturas)

def calc_prom_temp(matriz):
    suma = sum(matriz)
    prom = suma / len(matriz)
    print(f'El promedio de la temperatura de esta semanada es de: {round(prom,2)}.')

lista()
calc_prom_temp(matriz_temp)


