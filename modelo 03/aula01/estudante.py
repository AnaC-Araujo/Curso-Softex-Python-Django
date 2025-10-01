'''Seu trabalho aqui:
● Crie uma classe chamada Estudante que herda (pega emprestado) todas as
características da classe Pessoa.
● Adicione um atributo de matrícula a esta classe.
● Para guardar as notas, use um dicionário, onde a "chave" é o nome da matéria (como
'Matemática') e o "valor" é uma lista de notas (ex: [9.0, 8.5]).
● Crie um método "setter" para adicionar notas a uma matéria específica. Um "setter" é
uma forma de definir ou alterar uma informação dentro do objeto.'''

from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self._matricula = matricula
        self.notas = {}

    @property
    def matricula(self):
        return self._matricula
    
    def adicionar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    @property
    def mostrar_informacoes(self):
        return {
            "Nome": self._nome,
            "Idade": self._idade,
            "Matrícula": self._matricula,
            "Notas": self.notas
            }
    
'''aluno01 = Estudante("Juquinha", 18, 202)
aluno02 = Estudante("Josefaldo", 20, 200)
aluno03 = Estudante("Josefa", 21, 203)

a01.adicionar_nota("Português", 9.5)
aluno01.adicionar_nota("Matemática", 10)

aluno02.adicionar_nota("Português", 8)
aluno02.adicionar_nota("Matemática", 7)

aluno01.mostrar_informacoes()'''