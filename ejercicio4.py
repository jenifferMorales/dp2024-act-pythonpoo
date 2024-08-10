class Herencia:
    def datos (self, nombre, edad):
        self.nombre = ""
        self.edad = 0

    def persona(self):
        print("El nombre de la persona es: ", self.nombre)
        print ("La edad es: ", self.edad)


#clase hija
class Ejemplo(Herencia):

    def datos(self):
        print("Estoy usando herencia")


herencia = Herencia()
herencia.nombre=str(input("Escriba su nombre"))
herencia.edad= int(input("Ingrese su edad"))
