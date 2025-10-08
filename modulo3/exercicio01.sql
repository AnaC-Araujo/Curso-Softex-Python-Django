CREATE Table autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE Table livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER
);
DROP TABLE livros;
CREATE Table autores_livros(
    id_autor INTEGER NOT NULL,
    id_livro INTEGER NOT NULL,
    FOREIGN key (id_autor) REFERENCES autores(id),
    FOREIGN key (id_livro) REFERENCES cursos(id)
);

INSERT INTO autores(nome, nacionalidade) VALUES ('Joãozinho', 'brasileiro');
INSERT INTO autores(nome, nacionalidade) VALUES ('Mariazinha', 'italiana');


INSERT INTO livros(titulo, ano_publicacao) VALUES ('Como montar meu banquinho', 2024);
INSERT INTO livros(titulo, ano_publicacao) VALUES ('Lógica do banquinho digital', 2025);
INSERT INTO livros(titulo, ano_publicacao) VALUES ('Continue com o seu baquinho', 2025);


INSERT INTO autores_livros(id_autor, id_livro) VALUES (1,1), (1,2), (2,3)

SELECT * FROM autores;
SELECT * FROM livros;
SELECT * FROM autores_livros;

SELECT autores.nome, livros.titulo FROM autores_livros
INNER JOIN autores ON autores_livros.id_autor = autores.id
INNER JOIN livros ON autores_livros.id_livro = livros.id;

SELECT count(livros.titulo) AS qnt_livros, autores.nome FROM autores_livros