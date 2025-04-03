from connection import get_connection
from operacoesbd import insertNoBancoDados


class Manifestacao:
    def __init__(self, descricao):
        self.descricao = descricao

    def inserir(self):
        connection = get_connection()

        sql = f"INSERT INTO {self.__class__.__name__} (descricao) VALUES ('{self.descricao}')"

        result = insertNoBancoDados(connection, sql)

        connection.close()

        return result

    def listar(self):
        pass

    def excluir(self, id):
        pass


class Sugestao(Manifestacao): ...


class Reclamacao(Manifestacao): ...


class Elogio(Manifestacao): ...
