/* Cria a tabela dados_paises */
CREATE TABLE dados_paises (
    id SERIAL PRIMARY KEY,
    pais VARCHAR(100),
    ano INT,
    valor NUMERIC NULL
);

/* Importa o arquivo .csv para o banco */
COPY dados_paises (pais, ano, valor)
FROM 'C:\\Users\\rafael\\Documents\\IDHistorico\\dados_transformados.csv'
DELIMITER ','
CSV HEADER;

/* Apagar todos os dados e reiniciar do zero */
TRUNCATE TABLE dados_paises RESTART IDENTITY;

/* seleciona as primeiras 5 linhas */
SELECT * FROM dados_paises LIMIT 20;




