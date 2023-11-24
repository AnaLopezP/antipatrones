'''Esta clase es la que se encarga de realizar las operaciones de la calculadora'''''

class Calculadora():
    #inicializamos los atributos
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    #función que hace la suma (si por alguna razón no se puede sumar, devuelve un mensaje de error)
    def suma(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 + self.numero2
        
        except ValueError:
            return "Error en la suma"
        
    #función que hace la resta (si por alguna razón no se puede sumar, devuelve un mensaje de error)
    def resta(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 - self.numero2
        
        except ValueError:
            return "Error en la resta"
        
    #función que hace la multiplicación (si por alguna razón no se puede sumar, devuelve un mensaje de error)
    def multiplicacion(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 * self.numero2
        
        except ValueError:
            return "Error en la multiplicacion"

    #función que hace la división (si por alguna razón no se puede sumar, devuelve un mensaje de error)    
    def division(self):
        try:
            print('miau')
            self.numero1 = float(self.numero1)
            self.numero2 = float(self.numero2)
            if self.numero2!= 0:
                return self.numero1 / self.numero2
            else:
                return "No se puede dividir entre 0, imbécil"
        except ValueError:
            return "Error en la division"
        
            