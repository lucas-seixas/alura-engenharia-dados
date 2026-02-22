import csv
import json


class Dados:
    def __init__(self, path, tipo_dados):
        self.__path = path
        self.__tipo_dados = tipo_dados
        self.dados = self.__leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __leitura_json(self):
        dados_json = []
        with open(self.__path) as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(self):
        dados_csv = []
        with open(self.__path) as file:
            spamreader = csv.DictReader(file, delimiter=",")
            [dados_csv.append(row) for row in spamreader]
        return dados_csv

    def __leitura_dados(self):
        dados = []

        if self.__tipo_dados == "json":
            dados = self.__leitura_json()

        elif self.__tipo_dados == "csv":
            dados = self.__leitura_csv()

        elif self.__tipo_dados == "list":
            dados = self.__path
            self.__path = "lista em memoria"

        else:
            raise ValueError("Tipo de arquivo não suportado")

        return dados

    def __get_columns(self):
        return list(self.dados[-1].keys())

    def __size_data(self):
        return len(self.dados)

    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, "Indisponível"))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela

    # Métodos públicos
    def rename_columns(self, key_mapping):
        new_dados = [
            {key_mapping[old_key]: value for old_key, value in old_dict.items()}
            for old_dict in self.dados
        ]
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

    # @staticmethod
    # def join(dadosA, dadosB):
    #     combined_list = []
    #     combined_list.extend(dadosA.dados)
    #     combined_list.extend(dadosB.dados)
    #     return Dados(combined_list, "list")

    @classmethod
    def join(cls, objetos):
        # Assume que 'objetos' é uma lista ou iterável de objetos Dados
        combined_list = []
        for obj in objetos:
            if hasattr(obj, 'dados') and isinstance(obj.dados, list):
                combined_list.extend(obj.dados)
            else:
                raise ValueError("Todos os objetos devem ser instâncias de Dados com 'dados' como lista.")
        return cls(combined_list, 'list')

    def salvando_dados(self, path):
        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, "w") as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
            print(f"Dados salvos com sucesso em: {path}")
