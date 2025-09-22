
from math import pi
class Circulo:
    def __init__(self, raio:int):
        self._raio = raio
    
    @property
    def raio(self) -> int:
        return self._raio
    
    @raio.setter
    def raio(self, novo_raio: int) -> None:
        if novo_raio > 0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print("Digite um valor positivo e inteiro.")

    def calcular_area(self) -> float:
        area = pi * self._raio ** 2
        return print(f"{area:.3f}")
    
roda = Circulo(2)
print(roda.raio)
roda.raio = 6
roda.calcular_area()