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
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Cola()
        return cls._instance
    
    def __init__(self):
        self.cola = []

    def agregar_discapacitado(self, turno):
        self.cola.insert(0, turno)

    def agregar(self, turno):
        self.cola.append(turno)

class TurnoFactory:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = TurnoFactory()
        return cls._instance
    
    def obtener_turno(self, tipo_turno, posicion):
        if tipo_turno <= 0.1:
            return TurnoDiscapacitado(posicion, time.time())
        else:
            return Turno(posicion, time.time())

class TurnosFachada:
    
    def crear_cola(self, tam_cola):
        cola = Cola.get_instance()
        
        for i in range(tam_cola):
            turno_factory = TurnoFactory.get_instance()
            tipo_turno = random.random()
            turno = turno_factory.obtener_turno(tipo_turno, i)
            
            if tipo_turno <= 0.1:
                # Discapacitado
                cola.agregar_discapacitado(turno)
            else:
                # Turno
                cola.agregar(turno)

        return cola
                
    def servir_cola(self, cola):
        for i in range(len(cola.cola)):
            turno = cola.cola.pop(0)
            turno.atender()
            turno.imprimir()
        

def main():
    fachada = TurnosFachada()
    cola = fachada.crear_cola(int(sys.argv[1]))
    fachada.servir_cola(cola)

    


if __name__ == '__main__':
    main()

