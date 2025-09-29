class Teclado:
    def __init__(self):
        pass
    def ligar(self):
        print("O teclado está ativado!")

class Mouse:
    def __init__(self):
        pass
    def ligar(self):
        print("O mouse está ativado!")

class Monitor:
    def __init__(self):
        pass
    def ligar(self):
        print("O monitor está ativado!")

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()

    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()
        print("O computador está pronto para uso!")

computadorzinho = Computador()
computadorzinho.ligar_computador()