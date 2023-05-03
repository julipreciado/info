from PyQt5 import QtWidgets
import sys
#hola
from modelo import Sistema, client

from vista import Ventana

class comunicacion(object):
    def __init__(self):
        self.__app=QtWidgets.QApplication(sys.argv)
        self.__view=Ventana()
        self.system=Sistema(client)
        self.controller=ctrl(self.__view, self.system)
        self.__view.conexionconelcontrolador(self.controller)

    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec())

class ctrl(object):
    def __init__(self, view, system):
        self.__view=view
        self.system =system

    def agregarpacientes(self, cc, nombre, edad):
        if cc.isdigit()==True:
            self.system.cedula(cc)
        else:
            print("La cédula debe ser numérica")

        if nombre.isalpha() ==True:
            self.system.nombre(cc, nombre)
        else:
            print("El nombre sólo debe contener letras")
        
        if edad.isdigit()==True:
            self.system.edad(cc, edad)
        else:
            print("La edad debe ser numérica")

    def buscarensistema(self,cc):
        nombre,edad=self.system.verificar_db(cc)
        if nombre != None:
            self.__view.rellenar_datos(nombre, edad)
            return True
        else:
            print("El paciente no existe")
            return False
        

if __name__ =="__main__":
    controller=comunicacion()
    controller.main()

