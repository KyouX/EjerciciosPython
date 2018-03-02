class CalculadoraBinaria:
    def __init__(self, conversor):
        self.conversor = conversor
        
    def sumar(self, opbin1, opbin2):
        res = self.conversor.dtb(
            self.conversor.btd(opbin1) + self.conversor.btd(opbin2))
        return res
    
    def restar(self, opbin1, opbin2):
        res = self.conversor.dtb(
            self.conversor.btd(opbin1) - self.conversor.btd(opbin2))
        return res
