"""
Este módulo contém a classe Manifestacao e suas subclasses: Sugestao, Reclamacao e Elogio.
"""

from connection import get_connection
from operacoesbd import insertNoBancoDados


class Manifestacao:
    def __init__(self, descricao):
        self.descricao = descricao

    def inserir(self):
        connection = get_connection()

        # usado o self.__class__.__name__ para pegar o nome da classe
        sql = f"INSERT INTO Manifestacao (descricao, tipo) VALUES ('{self.descricao}', '{self.__class__.__name__}')"

        result = insertNoBancoDados(connection, sql)

        connection.close()

        return result

class Sugestao(Manifestacao):
    ...


class Reclamacao(Manifestacao):
    ...


class Elogio(Manifestacao):
    ...
