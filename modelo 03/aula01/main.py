'''Seu trabalho aqui:
● Importe as classes Escola e Estudante que você criou.
● Crie uma instância (um objeto) da sua Escola.
● Crie pelo menos dois objetos da sua classe Estudante, dando a cada um um nome, idade
e matrícula.
● Use os métodos que você criou para:
○ Adicionar algumas matérias e notas para cada estudante.
○ Adicionar os estudantes à sua Escola.
● Chame o método mostrar_relatorio() da sua Escola para ver a mágica acontecer!'''

from escola import Escola
from estudante import Estudante

escola = Escola("Tecnology")

aluno01 = Estudante("Juquinha", 18, 202)
aluno02 = Estudante("Josefaldo", 20, 200)
aluno03 = Estudante("Josefa", 21, 203)

aluno01.adicionar_nota("Português", 10)
aluno01.adicionar_nota("Matemática", 8)
aluno02.adicionar_nota("Geografia", 8)
aluno02.adicionar_nota("Matemática", 6.5)
aluno03.adicionar_nota("Geografia", 5)
aluno03.adicionar_nota("Matemática", 10)

