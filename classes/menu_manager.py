class Manager(object):

    @classmethod
    def encontrarLugar(cls,m,c):
        for x in m:
            if x.codigo==c:
                return x
            else:
                return x.encontrarLugar(c)
        return False