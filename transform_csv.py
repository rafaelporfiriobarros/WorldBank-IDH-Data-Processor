import pandas as pd

# Caminho do arquivo CSV original
input_csv = "IDHhistorico.csv"  # Substitua pelo caminho correto
output_csv = "dados_transformados.csv"

# Tentar detectar o delimitador automaticamente
with open(input_csv, "r", encoding="utf-8") as f:
    first_line = f.readline()
    delimiter = ";" if ";" in first_line else ","

# Carregar os dados com o delimitador correto
df = pd.read_csv(input_csv, delimiter=delimiter)

# Remover colunas sem nome
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Salvar novamente
df.to_csv("dados_transformados.csv", index=False)


# Corrigir possíveis problemas nos nomes das colunas
df.columns = df.columns.str.strip()  # Remove espaços extras

# Verificar o nome exato da coluna
print(df.columns)  # Isso ajudará a identificar se "IdPais" está correto

# Caso a coluna tenha um nome diferente, ajuste aqui:
if "IdPais" not in df.columns:
    for col in df.columns:
        if "pais" in col.lower():  # Procura algo parecido com "IdPais"
            df.rename(columns={col: "IdPais"}, inplace=True)

# Agora transformar os dados para formato LONG
df_long = df.melt(id_vars=["IdPais"], var_name="Ano", value_name="Valor")

# Substituir ".." por NaN (valores ausentes)
df_long["Valor"] = pd.to_numeric(df_long["Valor"], errors="coerce")

# Renomear coluna IdPais
df_long.rename(columns={"IdPais": "Pais"}, inplace=True)

# Salvar arquivo transformado
df_long.to_csv(output_csv, index=False)

print(f"Arquivo transformado salvo como: {output_csv}")
