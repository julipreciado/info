class Cosa:
    def __init__(self, publico:str, *, protegido: str = "protegido", privado: str= "privado"):
        self.publico = publico
        self._protegido = protegido
        self.__privado= privado

    def informacion(self):
        print(
            (
                f"Esta es una clase con atributos públicos : {self.publico}"
                f"un atributo protegido: {self._protegido}"
                f"y un atributo privado: {self.__privado}"
            )
        )

        
    def revelar_privado(self):
        return f"El atributo privado es {self.__privado}"

cosa=Cosa("público")
print(cosa.publico)

#print(cosa.__privado)

print(cosa._protegido)