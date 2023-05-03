import pymongo
client = pymongo.MongoClient("mongodb+srv://julipreciado:1234@cluster0.p75sqrz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

class Sistema():
    def __init__(self, client):
        mydb=client["Hospital"]
        self.__neurologia=mydb["neurologia"]

    def verificar_db(self, cedula):
        x=self.__neurologia.find_one({"Cédula":cedula})
        if x==None:
            return None, None
        else:
            return x["Nombre"], x["Edad"]
        
    def cedula(self, cedula):
        x=self.__neurologia.insert_one({"Cédula":cedula})

    def nombre(self, cedula, nombre):
        myquery={"Cédula":cedula}
        newvalues={"$set":{"Nombre":nombre}}
        self.__neurologia.update_one(myquery, newvalues)
    
    def edad(self, cedula, edad):
        myquery={"Cédula": cedula}
        newvalues={"$set":{"Edad":edad}}
        self.__neurologia.update_one(myquery, newvalues)