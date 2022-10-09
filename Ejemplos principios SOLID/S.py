#Ejemplo sin única responsabilidad:

from lib2to3.pytree import convert


class pato:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar (self):
        print(f"{self.nombre} no está volando muy alto")

    def nadar(self):
        print(self.nombre+" nada en el lago")

    def sonido(self)->str:
        return "Cuack"
    
    def saludar (self, patoDos:pato):
        print (f"{self.nombre}: {self.sonido()}, hola! {patoDos.nombre}")


# Ejemplo con única responsabilidad

class Pato:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar (self):
        print(f"{self.nombre} no está volando muy alto")

    def nadar(self):
        print(self.nombre+" nada en el lago")

    def sonido(self)->str:
        return "Cuack"

class comunicador: 
    
    def __init__(self, canal):
        self.canal = canal

    def comunicarse (self, pato1:Pato, pato2:Pato):
        palabraUno = f"{pato1.nombre}:{pato1.sonido()}, hola {pato2.nombre}"
        palabraDos = f"{pato2.nombre}:{pato2.sonido()}, hola {pato1.nombre}"
        conversacion = [palabraUno,palabraDos]

        print (*conversacion, f"(via{self.canal})", sep = '\n')
