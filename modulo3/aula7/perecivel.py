from item_iventario import ItemInventario

class Perecivel(ItemInventario):
    def __init__(self, nome, quantidade, valor_unitario, data_validade: str):
        super().__init__(nome, quantidade, valor_unitario)
        self.data_validade = data_validade

    def __str__(self):
        return f"{self.nome} - \nQuantidade: {self.quantidade} \nValor Unitário: R$ {self.valor_unitario} \nValidade: {self.data_validade}"