
class Caja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_productos = []
            
    def añadir_producto(self, producto, cantidad, precio):
        self.lista_de_productos.append((producto, (cantidad * precio)))
    
    def total_de_la_compra(self):
        self.suma = 0
        
        for i in self.lista_de_productos:
            self.suma += i[1]
            
        print(f'El total de la compra es de {round(self.suma,2)}.')    

encargado = Caja('Jinsonp')     
encargado.añadir_producto('Manzanas', 0.35, 5)      
encargado.añadir_producto('Leche 1 Litro', 1.10, 3)
encargado.añadir_producto('Cereal Chocapic 500 gr', 2.36, 1)
encargado.añadir_producto('Jarra Cerámica', 2.53, 2)
encargado.añadir_producto('Fideos Julian', 1.86, 2)

encargado.total_de_la_compra()

        
            
        
        
        

        
        
    
         
      

    


        
    