class Circulo:
    def __init__(self, raio:int):
        self.raio = raio
    
    @property
    def raio(self):
        return self.raio
    
    @raio.setter
    def raio(self, valor_raio: int):
        if valor_raio > 0:
            self.raio = valor_raio
        else:
            print("Digite um valor positivo.")

    def calcular_area():
        