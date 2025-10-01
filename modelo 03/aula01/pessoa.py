'''Toda escola tem pessoas. Um estudante é uma pessoa, um professor é uma pessoa. Vamos
criar um "molde" básico para qualquer pessoa.
Seu trabalho aqui:
● Crie uma classe (o nosso molde) chamada Pessoa.
● Essa classe deve ter um nome e uma idade.
● Para garantir que as informações sejam acessadas e modificadas de forma organizada,
implemente um método "getter" para o nome. Um "getter" é uma forma de obter a
informação de um objeto.'''

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
'''a1 = Pessoa("Juquinha", 18)
a2 = Pessoa("Josefaldo", 20)
a3 = Pessoa("Josefa", 21)

print ("****** Alunos ******")
print(f"\nAluno: {a1.nome} \nIdade: {a1.idade}")
print(f"\nAluno: {a2.nome} \nIdade: {a2.idade}")
print(f"\nAluno: {a3.nome} \nIdade: {a3.idade}")'''