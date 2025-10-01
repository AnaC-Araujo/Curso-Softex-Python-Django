'''Seu trabalho aqui:
● Crie uma classe chamada Escola.
● Esta classe deve ter uma lista para guardar todos os objetos Estudante.
● Crie um método adicionar_estudante() para colocar novos estudantes na lista da escola.
● Crie um método mostrar_relatorio() que percorre a lista de estudantes e imprime todas
as suas informações: nome, matrícula, e as notas de cada matéria.
'''
from estudante import Estudante

class Escola:
    def __init__(self, nome_escola:str):
        self.nome_escola = nome_escola

    def adicionar_estudante(self, estudante: Estudante):
        self.estudantes = []
        self.estudantes.append(estudante)

    def mostrar_relatorio(self):
        for estudante in self.estudantes:
            print(f"\nNome: {estudante.nome} \nMatrícula: {estudante.matricula} \nNotas: {estudante.notas}")
        else:
            print("Não há estudantes!")