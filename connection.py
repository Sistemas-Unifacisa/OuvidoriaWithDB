from operacoesbd import criarConexao


def get_connection():
    connection = criarConexao(
        endereco="localhost", usuario="root", senha="admin", bancodedados="test_db"
    )

    return connection
...