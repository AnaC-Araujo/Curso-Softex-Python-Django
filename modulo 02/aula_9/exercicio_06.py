class Musica:
    def __init__(self, titulo:str, artista:str):
        self.titulo = titulo
        self.atista = artista

class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"A música '{musica.titulo}' foi adicionada na playlist.")

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"A música '{musica.titulo}' do artista {musica.artista} foi removida da sua playlist.")
        else:
            print(f"A música '{musica.titulo}' não se encontra na playlist.")
    
    def tocar_playlit(self, musica):
        if musica in self.musicas:
            print(f"Tocando {musica.titulo} de {musica.artista}.")
        else:
            print("Playlist pausada.")

playlist = Playlist()

m1 = Musica("Melhor só", "Baco Exu do Blues")
m2 = Musica("Flamingos", "Baco Exu do Blues")

playlist.adicionar_musica(m1)
playlist.adicionar_musica(m2)

playlist.tocar_playlit(m1)