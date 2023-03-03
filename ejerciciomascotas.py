import pymongo

class Medicamento():
    def __init__(self,client):
        mydb =client ["sistVete"]
        self.__medicamentos = mydb["medicamentos"]

    def verNombre(self):
        for x in self.__medicamentos.find():
            return print(x)
    
    def asignarInfoMed(self, nombre_med, dosis):
        self.__medicamento = self.__medicamentos.insert_one({"Nombre": nombre_med}) 
        self.__medicamento = self.__medicamentos.insert_one({"Dosis": dosis})
        return self.__medicamento


class Mascota(Medicamento):
    def __init__(self, client):
        Medicamento.__init__(client)
    
       
    def asignarNombreMascota(self,temp):
        self.__nombre = temp  

    def verNombre(self):
        return self.__nombre
    
    def asignarTipo(self,temp):
        self.__tipo = temp 
        
    def asignarHistoria(self,temp):
        self.__num_historia = temp 
    def verHistoria(self):
        return self.__num_historia
        
    def asignarPeso(self,temp):
        self.__peso = temp 
        
    def asignarFechaIngreso(self,temp):
        self.__fecha_ingreso = temp 
    def verFechaIngreso(self):
        return self.__fecha_ingreso 

    def asignarMedicamentos(self,m):
        self.__lista_medicamentos = m
    def verMedicamentos(self):
        return self.__lista_medicamentos







def main():
    client = pymongo.MongoClient("mongodb+srv://julipreciado:1234@cluster0.p75sqrz.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    nm=int(input("Ingrese la cantidad de medicamento de la mascota: "))
    m=0
    while m<nm:
        nombre_medicamentos  = input("Ingrese el nombre: ")
        dosis = input("Ingrese la dosis: ")
        medicamento= Medicamento(client)
        medicamento.asignarNombreDosis(nombre_medicamentos, dosis)
        medicamento.verNombre("Dólex")
        m+=1

if __name__=="__main__":
    main()