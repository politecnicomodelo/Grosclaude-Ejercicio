from .barrio import Barrio
from .lugar import Lugar
class Ciudad(Lugar):

    def agregarContenido(self,c,n,co,p):
        self.contenido.append(Barrio(c,n,co,p))