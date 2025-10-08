CREATE Table professor(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE Table alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN key (id_professor) REFERENCES professor(id)
);