"""
Este arquivo contém a função get_connection, que é responsável por criar uma conexão com o banco de dados MySQL.
A biblioteca operacoesbd é utilizada para criar a conexão.

Também contém a função load_database_config, que cria as tabelas necessárias para o funcionamento do sistema de Ouvidoria.
As tabelas criadas são: Sugestao, Reclamacao e Elogio.
"""

from operacoesbd import criarConexao


def get_connection():
    connection = criarConexao(
        endereco="localhost", usuario="root", senha="admin", bancodedados="OuvidoriaDB"
    )

    return connection

def ensure_table_exists(cursor, table_name, create_table_sql):
    """
    Verifica se uma tabela existe e a cria caso não exista.
    """

    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()

    if result:
        print(f"Tabela '{table_name}' já existe.")
    
    else:
        cursor.execute(create_table_sql)
        print(f"Tabela '{table_name}' criada com sucesso.")

def load_database_config():
    """
    Cria as tabelas necessárias para o funcionamento do sistema de Ouvidoria.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Define as tabelas e seus comandos de criação
    tables = {
        "Sugestao": """
            CREATE TABLE Sugestao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """,
        "Reclamacao": """
            CREATE TABLE Reclamacao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """,
        "Elogio": """
            CREATE TABLE Elogio (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """
    }

    # Verifica e cria cada tabela
    for table_name, create_table_sql in tables.items():
        ensure_table_exists(cursor, table_name, create_table_sql)

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()