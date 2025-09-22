class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        # Isistance verifica se o primeiro é do tipo do segundo
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome
        else:
            print("O novo nome deve ser uma string não vazia.")

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade: int):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Digite apenas números inteiros e positivos.")


nova_pessoa = Pessoa("Josefa", 20)
print(nova_pessoa.nome)
print(nova_pessoa.idade)

nova_pessoa.nome = ""
nova_pessoa.idade = 50

print(nova_pessoa.nome)
print(nova_pessoa.idade)
