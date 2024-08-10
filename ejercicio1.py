class Textos:
    #atributos
    texto1= ""
    texto2= ""
    texto3=""
    #métodos
   
    def longitud (self):
        self.long1= len(self.texto1)
        self.long2= len(self.texto2)
        self.long3= len(self.texto3)
        print("La longitud del texto 1 es: ", self.long1 )
        print("La longitud del text0 2 es: ", self.long2 )
        print("La longitud del texto 3 es: ", self.long3 )
        self.promedio = (self.long1 + self.long2 + self.long3) / 3
        print("El promedio de las longitudes es: ", self.promedio)
    
    def concatenar(self):
        self.sumar = self.long1+self.long2+self.long3
        print("La suma de las longitudes es: ", self.sumar)
        if self.sumar>=15:
              print("El texto tiene una longitud mayor a 15")
        else:
             print("El texto tiene una longitud menor a 15") 
    
    def caracteres(self):
         if self.long1> self.long2 and self.long1> self.long3:
              print("El texto mayor es: ", self.texto1, "con ", self.long1, " caracteres")
         elif self.long2> self.long1 and self.long2>self.long3:
              print("El texto mayor es: ", self.texto2, "con ", self.long2, " caracteres")
         else:
              print("El texto mayor es: ", self.texto3, "con ", self.long3, " caracteres")
    def numero(self):
         import re
         numeros = re.findall(r'\d+', self.texto1)
         print("Los numeros encontrados en el texto 1 son: ", numeros)
         numeros2 = re.findall(r'\d+', self.texto2)
         print("Los numeros encontrados en el texto 2 son: ", numeros2)
         numeros3 = re.findall(r'\d+', self.texto3)
         print("Los numeros encontrados en el texto 2 son: ", numeros3)

              
          
      
        




frase = Textos()
frase.texto1 = str(input("Ingrese un texto\n"))
frase.texto2 = str(input("Ingrese un texto\n"))
frase.texto3 = str(input("Ingrese un texto\n"))
frase.longitud()
frase.concatenar()
frase.caracteres()
frase.numero()

    

