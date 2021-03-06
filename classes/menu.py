from .menu_manager import Manager
from .continente import Continente
class Menu(object):

    def __init__(self):
        self.continentes=[]

    def imprimirMenu(self):
        x=0
        print("1:Ver lugares")
        print("2:Agregar")
        print("3:Modificar")
        print("4:Borrar")
        x=input()
        if x=="1":
            self.opcion1()
        elif x=="2":
            self.opcion2()
        elif x=="3":
            self.opcion3()
        elif x=="4":
            self.opcion4()
    def opcion1(self):
        cod=input("Ingrese codigo de lugar: ")
        lugar=Manager.encontrarLugar(self.continentes,cod)
        if lugar==False:
            print("No se encontro ese lugar")
        else:
            print("Codigo:",lugar.codigo,
                  " Nombre:",lugar.nombre)
            print("Coordenadas:")
            for x in lugar.coordenadas:
                print(x)
            if lugar.__class__.__name__=="Barrio":
                print("Poblacion:",lugar.poblacion)
        self.imprimirMenu()

    def opcion2(self):
        obj=input("Que desea agregar: "
                  "1:Continente "
                  "2:Pais "
                  "3:Provincia "
                  "4:Ciudad "
                  "5:Barrio")
        c = input("Ingrese codigo:")
        n = input("Ingrese nombre:")
        co=[]
        while True:
            print("Para dejar de ingresar ingrese -1 en x o en y")
            x = input("Ingrese coordenada en x:")
            y = input("Ingrese coordenada en y:")
            if int(x)<0 or int(y)<0:
                break
            co.append((x,y))
        if obj!="1":
            l=input("Ingrese codigo a donde pertenece:")
            if Manager.encontrarLugar(self.continentes,l)== False:
                print("No se encontro ese lugar")
            elif Manager.encontrarLugar(self.continentes,l).__class__.__name__=="Barrio":
                print("No se puede añadir, porque es un barrio")
            elif Manager.encontrarLugar(self.continentes,l).__class__.__name__=="Ciudad":
                p=input("Ingrese poblacion:")
                Manager.encontrarLugar(self.continentes, l).agregarContenido(c,n,co,p)
            else:
                Manager.encontrarLugar(self.continentes, l).agregarContenido(c, n, co)
        else:
            self.continentes.append(Continente(c,n,co))
        self.imprimirMenu()

    def opcion3(self):
        cod = input("Ingrese codigo de lugar: ")
        lugar = Manager.encontrarLugar(self.continentes, cod)
        if lugar == False:
            print("No se encontro ese lugar")
        else:
            print("Deje en blanco si no quiere modificar")
            c = input("Ingrese codigo nuevo:")
            n = input("Ingrese nombre nuevo:")
            co = []
            while True:
                print("Para dejar de ingresar ingrese -1 en x o en y")
                x = input("Ingrese coordenada en x:")
                y = input("Ingrese coordenada en y:")
                if x!="" and y!="":
                    if int(x) < 0 or int(y) < 0:
                        break
                    co.append((x, y))
                break
            if lugar.__class__.__name__=="Barrio":
                p = input("Ingrese poblacion nueva:")
                if p !="":
                    lugar.poblacion=p
            if c != "":
                lugar.codigo = c
            if n != "":
                lugar.nombre = n
            if co!=[]:
                lugar.coordenadas=co
        self.imprimirMenu()
    def opcion4(self):
        cod=input("Ingrese codigo de lugar: ")
        lugar=Manager.encontrarLugar(self.continentes,cod)
        if lugar==False:
            print("No se encontro ese lugar")
        else:
            print("Se ha eliminado",Manager.eliminarLugar(self.continentes,cod))
        self.imprimirMenu()