class Sueldo:
    sueldo = 0.0
    venta = 0.0
    

    def comision(self):
        self.resultado = self.venta * 0.10
        print("La comisión ganada es: ", self.resultado)
    def igss(self):
        self.igss = self.sueldo * 0.0483
        print("El descuento de IGSS es: ", self.igss) 
    def ahorro(self):
        self.ahorro = (self.sueldo + self.venta) * 0.07
        print("El ahorro de este mes es: ", self.ahorro)
    def total(self):
        self.total = self.sueldo + self.venta + self.igss
        print("El total ganado este mes sin descuentos es: ", self.total)
    def descuentos(self):
        self.descuento = self.ahorro + self.igss
        print("El descuento total de este mes es: ", self.descuento)
    def liquido(self):
        self.liquido = self.total - self.descuento
        print("El sueldo liquido a recibir este es es: ", self.liquido)

        




dinero = Sueldo()
dinero.sueldo= int(input("Ingrese el sueldo: "))
dinero.venta = int(input("Ingrese las ventas: "))
dinero.comision()
dinero.igss()
dinero.ahorro()
dinero.total()
dinero.descuento()
dinero.liquido()