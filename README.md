# WorldBank IDH Data Processor

Este projeto é um script em Python que processa e transforma dados históricos de **Índice de Desenvolvimento Humano (IDH)**, obtidos do [World Bank DataBank](https://databank.worldbank.org/indicator/FP.CPI.TOTL.ZG/1ff4a498/Popular-Indicators#). O script realiza a limpeza, organização e transformação dos dados de um formato "wide" para "long", facilitando análises posteriores.

---

## 📋 Descrição do Projeto

O script foi desenvolvido para processar um arquivo CSV contendo dados históricos de IDH. Ele realiza as seguintes etapas:

1. **Leitura do arquivo CSV**:
   - Detecta automaticamente o delimitador (`,` ou `;`).
   - Remove colunas sem nome (geradas automaticamente pelo Pandas).

2. **Limpeza dos dados**:
   - Remove espaços extras nos nomes das colunas.
   - Corrige possíveis problemas nos nomes das colunas (por exemplo, renomeia colunas que contenham "pais" para "IdPais").

3. **Transformação dos dados**:
   - Converte os dados de formato "wide" para "long" usando a função `melt` do Pandas.
   - Substitui valores ausentes representados por `".."` por `NaN`.

4. **Salvamento dos dados transformados**:
   - Gera um novo arquivo CSV (`dados_transformados.csv`) com os dados no formato "long", pronto para análise.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (linguagem de programação)
- **Pandas** (biblioteca para manipulação de dados)
- **CSV** (formato de arquivo de entrada e saída)

---

## 📂 Estrutura do Projeto

O projeto consiste em um único script Python (`transform_idh_data.py`) e um arquivo CSV de exemplo (`IDHhistorico.csv`). Após a execução, o script gera um novo arquivo CSV (`dados_transformados.csv`).



---

## 🚀 Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/WorldBank-IDH-Data-Processor.git
   cd WorldBank-IDH-Data-Processor


2. Instale as dependências:

Certifique-se de ter o Python instalado. Em seguida, instale o Pandas:

pip install pandas

3.  Execute o script:

Coloque o arquivo IDHhistorico.csv na pasta do projeto e execute o script:

python transform_idh_data.py

4. Verifique o resultado:

Após a execução, o arquivo dados_transformados.csv será gerado na pasta do projeto.

## 📊 Exemplo da Transformação dos dados

### Formato Original (Wide)

| IdPais | 2000 | 2001 | 2002 | 2003 |
|--------|------|------|------|------|
| BRA    | 0.69 | 0.70 | 0.71 | 0.72 |
| USA    | 0.90 | 0.91 | 0.92 | 0.93 |

### Formato Transformado (Long)

| Pais | Ano  | Valor |
|------|------|-------|
| BRA  | 2000 | 0.69  |
| BRA  | 2001 | 0.70  |
| BRA  | 2002 | 0.71  |
| USA  | 2000 | 0.90  |
| USA  | 2001 | 0.91  |

- Dados obtidos do [World Bank DataBank](https://databank.worldbank.org/indicator/FP.CPI.TOTL.ZG/1ff4a498/Popular-Indicators#).