class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def potencia(self):
        self.resultado = "La potencia de " + str(self.num1) + " elevado a " + str(self.num2) + " es igula a " + str(self.num1**self.num2)


    def raiz(self):
        if self.num2 == 0:
            self.resultado = "Error: el índice de la raíz no puede ser 0"
        elif self.num1 < 0 and self.num2 % 2 == 0:
            self.resultado = "Error: no se puede calcular raíz par de un número negativo"
        else:
            self.resultado = f"La raíz {self.num2}-ésima de {self.num1} es igual a {self.num1 ** (1 / self.num2)}"
        return self.resultado
    
    def mostrarResultado(self):
        print(self.resultado)
