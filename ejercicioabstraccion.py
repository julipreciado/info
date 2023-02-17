class Persona():
    def __init__(self):
        self.__nombre= ""
        self.__cedula= 0
        self.__genero= ""


    def asignarNombre(self,rol):
        self.__nombre = input("Ingrese el nombre del " +rol + ":")
    def asignarCedula(self, rol):
        self.__cedula = int(input("Ingrese la cédula del " +rol + ":"))
    def asignarGenero(self,rol):
        self.__genero = input("Ingrese el género del " +rol + ":" )
    
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def imprimirInfo(self):
        print(self.__nombre, self.__cedula, self.__genero)
    def guardarInfo(self):
        return self.__nombre, self.__cedula, self.__genero



class Sistema(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__lista_pacientes = []
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []

    def numPacientes(self):
        self.__numero_pacientes =len(self.__lista_pacientes)
        return self.__numero_pacientes
    
    


    def ingresarPacientes(self, rol):
        p=Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio()
        self.__lista_pacientes.append(p.guardarInfo())
        self.__lista_nombre.append(p.verNombre())
        self.__lista_cedula.append(p.verCedula())
        self.__lista_genero.append(p.verGenero())
        print(self.__lista_pacientes)
        print(self.numPacientes())
        

    def verDatosPacientesLista(self):
        cedula =str(input("Ingresar la cédula del Paciente que busca en la lista: "))
        for c in self.__lista_pacientes:
            if cedula == str(c[1]):
                return print(c)
 

class Paciente(Persona):
    def __init__(self):
        self.__servicio =""
    def asignarServicio(self):
        self.__servicio =input("Ingresar el servicio: ")
    def verServicio(self):
        return self.__servicio

    

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self) 
        self.__turno = {"Mañana":"7-19", "Noche":"19-7", "Corrido":"Corrido"}
    def asignarTurno(self, turno):
        self.__turno = turno
    def verturno(self, turno):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        self.__rango = ""
    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self, rango):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        self.__especialidad = ""
    def asignarEspecialidad(self, especialidad):
        self.__especialidad= especialidad
    def verEspecialidad(self):
        return self.__especialidad


def main():
    s=Sistema()
    while True:
        op =int(input("""
        1.Nuevo paciente 
        2.Número de pacientes 
        3.Datos Paciente 
        4.Salir
        >"""))
        if op==1:
            s.ingresarPacientes("Paciente")
        elif op==2:
            print("Ahora hay: " + str(s.numPacientes()))
        elif op==3:
            s.verDatosPacientesLista()
        elif op==4:
            break
        else:
            print("Opcion inválida")

if __name__=="__main__":
    main()