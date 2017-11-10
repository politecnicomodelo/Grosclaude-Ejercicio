from .provincia import Provincia
from .lugar import Lugar
class Pais(Lugar):

    def agregarContenido(self,c,n,co):
        self.contenido.append(Provincia(c,n,co))