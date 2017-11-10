from .pais import Pais

class Continente(object):

    def __init__(self, c, n, co):
        self.codigo=c
        self.nombre=n
        self.coordenadas=co
        self.contenido=[]

    def getPoblacion(self):
        p=0
        for x in self.contenido:
            p+=x.getPoblacion()
        return p

    def encontrarLugar(self,c):
        for x in self.contenido:
            if x.codigo==c:
                return x
            else:
                return x.encontrarLugar(c)
        return False


    def agregarContenido(self,c,n,co):
        self.contenido.append(Pais(c,n,co))

    def eliminarLugar(self,c):
        for x in self.contenido:
            if x.codigo==c:
                self.contenido.remove(x)
                return True
            else:
                return x.encontrarLugar(c)
        return False