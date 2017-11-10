class Manager(object):

    @classmethod
    def encontrarLugar(cls,m,c):
        for x in m:
            if x.codigo==c:
                return x
            else:
                return x.encontrarLugar(c)
        return False
    @classmethod
    def eliminarLugar(cls,m,c):
        for x in m:
            if x.codigo==c:
                m.remove(x)
                return True
            else:
                return x.encontrarLugar(c)
        return False