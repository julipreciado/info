class ave:
    def __init__(self, tipo, vuela):
        self.ave=tipo
        self.vuelo=vuela
        self.oviparos=True
        self.pico=True
    def comer(self, comida):
        print("Este tipo de ave come normalmente : ", comida)

    def volar(self):
        print("Este tipo de ave puede volar : ", self.vuelo)


    

class ganso(ave):
    def __init__(self, tipo, vuela, accion, pata):
        ave.__init__(self, tipo, vuela)
        self.habilidad =accion
        self.patas=pata

    def destreza(self):
        print("Esta ave puede : ", self.habilidad)

class pato(ganso):
    pass

class gallina(ave):
    pass

p=ave("gallina", False)
p.volar()
p.comer("Maiz")

g=ganso("carnivoro", True, "nadar", "4")
g.destreza()


class Ejemplo:
    __atributo_privado="Soy un atributo inalcanzable desde fuera"
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera ")

    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado()

e=Ejemplo()
print(e.atributo_publico())
e.metodo_publico()