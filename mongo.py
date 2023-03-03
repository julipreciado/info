import pymongo
client = pymongo.MongoClient("mongodb+srv://julipreciado:1234@cluster0.p75sqrz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb=client["bbdd"]
mycol=mydb["clientes"]

mydict = {"nombre": "Maria", "direccion": 123}
#x=mycol.insert_one(mydict)
#print(x.inserted_id)

#for x in mycol.find({"direccion":1}):
#    print(x)

for y in mycol.find():
    print(y)

newvalues={"$set": {"nombre":"ppp"}}

mycol.update_one(mydict, newvalues)

#print "clientes" después del update:
for x in mycol.find():
    print(x)