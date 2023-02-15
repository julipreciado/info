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

    

class Paciente(Persona):
    def __init__(self):
        self.__servicio =""
    def asignarServicio(self, servicio):
        self.__servicio =input("Ingresar el servicio: ")
    def verServicio(self):
        return self.__servicio

class Sistema(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__lista_pacientes = []

    def numPacientes(self):
        self.__numero_pacientes =len(self.__lista_pacientes)
        return self.__numero_pacientes

def ingresarPacientes(self, rol):
        p=Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio()
        self.__lista_pacientes.append(p)
        print(self.numPacientes())



class Empleado_Hospital(Persona):
    def __init__(self):
        self.__turno = ""
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

m1=Medico()
m1.asignarEspecialidad("Pediatra")
print(m1.verEspecialidad())