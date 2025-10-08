CREATE TABLE professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
);

CREATE Table alunos(
    id INTEGER PRIMARY key,
    nome TEXT NOT NULL,
    id_professor INTEGER NOT NULL,
    FOREIGN key (id_professor) REFERENCES professores (id)
);

DROP TABLE 
INSERT INTO professores(nome) VALUES('Anderson');
INSERT INTO professores(nome) VALUES('Fabricio');
SELECT * FROM professores