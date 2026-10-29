class Banco:
    #Constructor
    def __init__(self,nombreBanco,numero,codigoInternacional,montoPrincipal):
        self.nombreBanco = nombreBanco
        self.numero = numero
        self.codigoInternacional = codigoInternacional
        self.montoPrincipal = montoPrincipal

    #Getters
    def getnombreBanco(self):
        return self.nombreBanco
    def getnumero(self):
        return self.numero
    def getcodigoInternacional(self):
        return self.codigoInternacional
    def getmontoPrincipal(self):
        return self.montoPrincipal
        
    #Setters
    def setnombreBanco(self,nombreBanco):
        if nombreBanco=="":
            print("Favor de escribir un nombre para el Banco Principal")
        else:
            self.nombreBanco=nombreBanco
            print("Nombre del Banco Principal Actualizado con exito.")
        
    #Metodos
    def mostrarinformacion(self):
        info = f"No.: {self.numero}\nNombre del Banco Principal: {self.nombreBanco}\nCodigo INternacional: {self.codigoInternacional}\nMonto: {self.montoPrincipal}"
        return info