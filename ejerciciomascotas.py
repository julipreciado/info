import pymongo

class Medicamento():
    def __init__(self,client):
        mydb =client ["sistVete"]
        self.__medicamentos = mydb["medicamentos"]

    def verNombreMed(self):
        Nombre=list(self.__medicamentos.find())
        return Nombre[-1]["Nombre"]
    
    def verDosis(self):
        Dosis=list(self.__medicamentos.find())
        print('La dosis suministrada es: ' + str(Dosis[-1]['Dosis']))
       

    def asignarNombreMed(self, nombre_med):
        x = self.__medicamentos.insert_one({"Nombre": nombre_med}) 
        
    def asignarDosis(self, nombre_med, dosis):
        myquery={"Nombre": nombre_med}
        newvalues = {"$set": {"Dosis": dosis}}
        self.__medicamentos.update_one(myquery, newvalues)
     


class Mascota():
    def __init__(self, client):
        mydb =client ["sistVete"]
        self.__mascotas = mydb["mascota"]
    
    def asignarHistoria(self,numhistoria):
        x=self.__mascotas.insert_one({'Número de historia ':numhistoria})

    def asignarNombreMascota(self, numhistoria, nombre_mas):
        myquery = {"Número de historia": numhistoria}
        newvalues = { "$set": { "Nombre":nombre_mas} }
        self.__mascotas.update_one(myquery, newvalues)  

    def verNombreMascota(self):
        Nombre=list(self.__mascotas.find())
        print('El nombre de la mascota es: ' + str(Nombre[-1]['Nombre']))
    
    def asignarTipo(self,tipo, numhistoria):
        myquery0 = {"Número de historia": numhistoria}
        newvalues0 = { "$set": { "Tipo":tipo} }
        self.__mascotas.update_one(myquery0, newvalues0)
        
    def verHistoria(self):
        Historia=list(self.__mascotas.find())
        return Historia[-1]['Número de historia']
        
    def asignarPeso(self,peso, numhistoria):
        myquery = {"Número de historia": numhistoria}
        newvalues = { "$set": { "Peso":peso} }
        self.__mascotas.update_one(myquery, newvalues) 
        
    def asignarFechaIngreso(self,fecha, numhistoria ):
        myquery = {"Número de historia": numhistoria}
        newvalues = { "$set": { "Fecha ingreso":fecha} }
        self.__mascotas.update_one(myquery, newvalues)
    def verFechaIngreso(self):
        Fecha=list(self.__mascotas.find())
        print('La fecha de ingreso de la mascota es: ' + str(Fecha[-1]['Fecha ingreso'])) 

    def asignarNumMedicamentos(self,m, numhistoria, nummedicamentos):
        myquery = {"Número de historia": numhistoria}
        newvalues = { "$set": { "Número medicamentos ":nummedicamentos} }
        self.__mascotas.update_one(myquery, newvalues)
        self.__lista_medicamentos = m

    def verNumMedicamentos(self):
        NumMedicamentos=list(self.__mascotas.find())
        print('La cantidad de medicamentos es: ' + str(NumMedicamentos[-1]['Número medicamentos'])) 







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