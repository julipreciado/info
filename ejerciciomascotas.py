import pymongo

class Medicamento():
    def __init__(self,client):
        mydb =client ["sistVete"]
        self.__medicamentos = mydb["medicamentos"]

    def verNombre(self):
        for x in self.__medicamentos.find():
            return print(x)
    
    def asignarNombreDosis(self, nombre_med, dosis):
        self.__medicamento = self.__medicamentos.insert_one({"Nombre": nombre_med, "Dosis": dosis})
        return self.__medicamento

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

    if __name__=="__main__":
        main()