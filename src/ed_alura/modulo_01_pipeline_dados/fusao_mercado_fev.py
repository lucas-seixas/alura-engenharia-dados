from processamento_dados import Dados

path_json = "data/raw/modulo_01_pipeline/dados_empresaA.json"
path_csv = "data/raw/modulo_01_pipeline/dados_empresaB.csv"

# ----------
# Extract
# ----------

print()

dados_empresaA = Dados(path_json, "json")
print(f"Colunas da empresa A: {dados_empresaA.nome_colunas}")
print(f"Tamanho dados empresa A: {dados_empresaA.qtd_linhas}")
print()

dados_empresaB = Dados(path_csv, "csv")
print(f"Colunas da empresa B: {dados_empresaB.nome_colunas}")
print(f"Tamanho dados empresa B: {dados_empresaB.qtd_linhas}")
print()

# ----------
# Transform
# ----------

key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda",
}

dados_empresaB.rename_columns(key_mapping)
print(f"Colunas da empresa B após renomeação: {dados_empresaB.nome_colunas}")
print()

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Colunas dados fusão: {dados_fusao.nome_colunas}")
print(f"Tamanho dados fusão: {dados_fusao.qtd_linhas}")
print()

# ----------
# Load
# ----------

path_dados_combinados = "data/processed/modulo_01_pipeline/dados_combinados.csv"
dados_fusao.salvando_dados(path_dados_combinados)
