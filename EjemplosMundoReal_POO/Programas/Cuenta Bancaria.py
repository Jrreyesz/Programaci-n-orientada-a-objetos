class CuentaBancaria:
    
    def __init__(self, titular, saldo): #Definimos los atributos de la clase
        self.titular = titular
        self.saldo = saldo
        
    def ver_saldo(self): #Creamos un metodo para ver el saldo
        print(f'El saludo de tu cuenta es {self.saldo}.')
        
    def deposito(self, cantidad_depositada): #Creamos un método para depositar
        self.saldo += cantidad_depositada
        print(f'Su saldo actual es de {self.saldo}.')
        
    def retirar(self, retiro): #creamos un método para retirar 
        if (self.saldo - retiro >= 0) and retiro > 0:
            self.saldo -= retiro
            print(f'Usted ha retirado {retiro}. Su saldo restante es de {self.saldo}')
        else:
            print('No tiene saldo suficiente en la cuenta.')
            
cuenta = CuentaBancaria('Jinsonp Romario Reyes Zambrano', 956)

cuenta.ver_saldo() #Llamamos al metodo para ver el dinero en la cuenta

cuenta.deposito(236) #Llamamos al metodo para depositar dinero en la cuenta

cuenta.retirar(588) #Llmamaos al metodo para retirar dinero de la cuenta

cuenta.retirar(604)

cuenta.retirar(20)
        