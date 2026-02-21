import csv
import json


def leitura_json(path):
    dados = []
    with open(path) as file:
        dados = json.load(file)
        return dados


def leitura_csv(path):
    dados = []
    with open(path) as file:
        spamreader = csv.DictReader(file, delimiter=",")
        [dados.append(row) for row in spamreader]
        return dados


def leitura_dados(path, tipo_arquivo):
    if tipo_arquivo == "json":
        return leitura_json(path)
    elif tipo_arquivo == "csv":
        return leitura_csv(path)
    else:
        raise ValueError("Tipo de arquivo não suportado")


def get_columns(dados):
    return list(dados[-1].keys())


def rename_columns(dados, key_mapping):
    new_dados_csv = []
    new_dados_csv = [
        {key_mapping[old_key]: value for old_key, value in old_dict.items()}
        for old_dict in dados
    ]
    return new_dados_csv


def size_data(dados):
    return len(dados)


def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list


def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            # Retornar indisponível caso a chave não exista, evitando erros
            linha.append(row.get(coluna, "Indisponível"))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela


def salvando_dados(dados, path):
    with open(path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(dados)
        print(f"Dados salvos com sucesso em: {path}")


path_json = "data/raw/modulo_01_pipeline/dados_empresaA.json"
path_csv = "data/raw/modulo_01_pipeline/dados_empresaB.csv"

# Iniciando a leitura dos dados

dados_json = leitura_dados(path_json, "json")
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f"Nome colunas dados json: {nome_colunas_json}")
print(f"Tamanho dados json: {tamanho_dados_json}")
print()

dados_csv = leitura_dados(path_csv, "csv")
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f"Nome colunas dados csv: {nome_colunas_csv}")
print(f"Tamanho dados csv: {tamanho_dados_csv}")
print()

# Transformando os dados em um formato unificado

key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda",
}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)
print()

dados_fusao = join(dados_json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(f"Nome colunas dados fusão: {nome_colunas_fusao}")
print(f"Tamanho dados fusão: {tamanho_dados_fusao}")
print()

# Salvando os dados unificados em um novo arquivo JSON

dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

path_dados_combinados = "data/processed/modulo_01_pipeline/dados_combinados.csv"

salvando_dados(dados_fusao_tabela, path_dados_combinados)
