"""
Este arquivo contém a função get_connection, que é responsável por criar uma conexão com o banco de dados MySQL.
A biblioteca operacoesbd é utilizada para criar a conexão.
"""

from operacoesbd import criarConexao


def get_connection():
    connection = criarConexao(
        endereco="localhost", usuario="root", senha="admin", bancodedados="OuvidoriaDB"
    )

    return connection
