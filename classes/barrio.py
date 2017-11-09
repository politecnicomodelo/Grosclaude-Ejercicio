from .continente import Continente
class Barrio(Continente):

    def __init__(self,c,n,co,p):
        self.poblacion=p
        Continente.__init__(c,n,co)

    def getPoblacion(self):
        return self.poblacion