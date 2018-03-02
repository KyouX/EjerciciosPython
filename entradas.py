import sys
import random
import time

class Turno:
    def __init__(self, posicion, tiempo):
        self.posicion = posicion
        self.tiempo_ingreso = tiempo
        self.tiempo_atencion = 0

    def atender(self):
        time.sleep(3)
        self.tiempo_atencion = time.time()

    def imprimir(self):
        print("El Turno {} tuvo una duración de espera de {} segundos".format( self.posicion,
            int(self.tiempo_atencion - self.tiempo_ingreso)))

class TurnoDiscapacitado:
    def __init__(self, posicion, tiempo):
        self.posicion = posicion
        self.tiempo_ingreso = tiempo
        self.tiempo_atencion = 0

    def atender(self):
        time.sleep(6)
        self.tiempo_atencion = time.time()

    def imprimir(self):
        print("El Turno {} tuvo una duración de espera de {} segundos".format( self.posicion,
            int(self.tiempo_atencion - self.tiempo_ingreso)))



class Cola:
    def __init__(self):
        self.cola = []

    def agregar_discapacitado(self, turno):
        self.cola.insert(0, turno)

    def agregar(self, turno):
        self.cola.append(turno)

def main():
    cola = Cola()
    for i in range(int(sys.argv[1])):
        tipo_turno = random.random()
        if tipo_turno <= 0.1:
            # Discapacitado
            cola.agregar_discapacitado(TurnoDiscapacitado(i, time.time()))
        else:
            # Turno
            cola.agregar(Turno(i, time.time()))

    for i in range(int(sys.argv[1])):
        turno = cola.cola.pop(0)
        turno.atender()
        turno.imprimir()


if __name__ == '__main__':
    main()

