'''Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. Adicione um
método exibir() que imprime o título e a duração.
Crie duas classes filhas, Musica e Video, que herdam de Midia:
● Musica deve ter um atributo adicional artista e sobrescrever o método exibir() para
incluir o nome do artista.
● Video deve ter um atributo adicional resolucao e sobrescrever o método exibir() para
incluir a resolução.
No script principal, crie um dicionário para organizar sua coleção de mídias, usando as
chaves 'musicas' e 'videos'. Crie objetos de Musica e Video e os adicione a suas respectivas
listas dentro do dicionário. Por fim, itere sobre as listas e chame o método exibir() para cada
item, demonstrando o polimorfismo de forma organizada.'''

class Midia:
    def __init__(self, titulo:str, duracao_seg:int):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"'{self.titulo}' - {self.duracao_seg}")

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista:str):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"'{self.titulo}' de {self.artista} - {self.duracao_seg}")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao:str):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"'{self.titulo}' - {self.duracao_seg} com resolução {self.resolucao}")

musica_01 = Musica("O destino não quis", 320, "Maneva")
#musica_02 = Musica("Ponto de equilíbrio", 639, "Ponto de equilíbrio")
video_01 = Video("Flamingos", 357, "4k")

colecao = {
    "musicas": [],
    "videos" : []
}

colecao["musicas"].append(musica_01)
colecao["videos"].append(video_01)

print(colecao)

for item in colecao.values():
    for midia in item:
        midia.exibir()