class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome):
        comodo = Comodo(nome)
        self.comodos.append(comodo)
        print(f"O cômodo '{nome}' foi incluído a casa.")

    def listar_comodo(self):
        if not self.comodos:
            print("Não há cômodos na casa!")
        else:
            for comodo in self.comodos:
                print(f"{comodo.nome}")


casinha = Casa()
casinha.adicionar_comodo("Sala")
casinha.adicionar_comodo("Cozinha")
casinha.adicionar_comodo("Quarto")
casinha.adicionar_comodo("Banheiro")

casinha.listar_comodo()