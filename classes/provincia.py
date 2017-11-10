from .ciudad import Ciudad
from .lugar import Lugar
class Provincia(Lugar):

    def agregarContenido(self,c,n,co):
        self.contenido.append(Ciudad(c,n,co))