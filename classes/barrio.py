from .lugar import Lugar


class Barrio(Lugar):

    def __init__(self, c, n, co, p):
        Lugar.__init__(c,n,co)
        self.poblacion=p

    def getPoblacion(self):
        return self.poblacion