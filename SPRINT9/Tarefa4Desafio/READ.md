```sql 
    -- Criando a tabela de fatos
    CREATE TABLE fato_filmes (
        id INTEGER PRIMARY KEY,
        budget REAL,
        revenue REAL,
        vote_average REAL,
        vote_count INTEGER,
        FOREIGN KEY(id) REFERENCES dim_genero(id),
        FOREIGN KEY(id) REFERENCES dim_artista(id),
        FOREIGN KEY(id) REFERENCES dim_filme(id)
    );

    -- Criando as tabelas de dimensões
    CREATE TABLE dim_genero (
        id INTEGER PRIMARY KEY,
        gender TEXT
    );

    CREATE TABLE dim_artista (
        id INTEGER PRIMARY KEY,
        main_actor TEXT,
        director TEXT
    );

    CREATE TABLE dim_filme (
        id INTEGER PRIMARY KEY,
        title TEXT,
        release_date TEXT
    );
```

- Essa modelagem organiza os dados de forma que seja possível analisar a receita dos filmes em relação a outros fatores, como o orçamento do filme, a voto médio, etc. Isso pode ajudar a entender quais fatores contribuem para o sucesso financeiro de um filme e gerar insights para a tomada de decisão.