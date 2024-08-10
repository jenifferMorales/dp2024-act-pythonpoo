class Binario:
    valor = 0

    def factorial(self):
        import math
        self.factorial = math.factorial(valor)
        print("El factorial de: ", valor, "es: ", self.factorial)

    def primo(self):
        for i in range(1,valor):
         if valor % i == 0:
            contador = contador + 1
            if contador >=2:
               print("El numero no es primo")
            else:
               print("El numero si es primo")

    def numeroBin(self):
       self.binario = bin(valor)
       print("El numero: ", valor, " en binario es: ", self.binario)

binario = Binario()
valor = int(input("Ingrese un valor del 1 hasta infinito"))
binario.factorial()
binario.primo()
binario.numeroBin()