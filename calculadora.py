class Calculadora():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def suma(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 + self.numero2
        
        except ValueError:
            return "Error en la suma"
        
    def resta(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 - self.numero2
        
        except ValueError:
            return "Error en la resta"
        
    def multiplicacion(self):
        try:
            self.numero1 = int(self.numero1)
            self.numero2 = int(self.numero2)
            return self.numero1 * self.numero2
        
        except ValueError:
            return "Error en la multiplicacion"
        
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
        
            