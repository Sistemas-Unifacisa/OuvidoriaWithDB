from connection import get_connection


def load_database_config():
    """
    Cria as tabelas necessárias para o funcionamento do sistema de Ouvidoria.

    TODO: Implement DRY principle to avoid code duplication.
    """

    connection = get_connection()

    # Verifica se existe a tabela Sugestao
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'Sugestao'")
    result = cursor.fetchone()

    if result:
        print("Tabela 'Sugestao' já existe.")
    else:
        # Cria a tabela Sugestao
        cursor.execute("""
            CREATE TABLE Sugestao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """)
        print("Tabela 'Sugestao' criada com sucesso.")

    # Verifica se existe a tabela Reclamacao
    cursor.execute("SHOW TABLES LIKE 'Reclamacao'")
    result = cursor.fetchone()
    if result:
        print("Tabela 'Reclamacao' já existe.")
    else:
        # Cria a tabela Reclamacao
        cursor.execute("""
            CREATE TABLE Reclamacao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """)
        print("Tabela 'Reclamacao' criada com sucesso.")

    # Verifica se existe a tabela Elogio
    cursor.execute("SHOW TABLES LIKE 'Elogio'")
    result = cursor.fetchone()

    if result:
        print("Tabela 'Elogio' já existe.")
    else:
        # Cria a tabela Elogio
        cursor.execute("""
            CREATE TABLE Elogio (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao TEXT NOT NULL
            )
        """)
        print("Tabela 'Elogio' criada com sucesso.")
