class ItemInventario:
    def __init__(self, nome: str, quantidade: int, valor_unitario: float):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def valor_total(self):
        return self.quantidade * self.valor_unitario