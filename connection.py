from operacoesbd import criarConexao, insertNoBancoDados, encerrarConexao

# Aprendendo a conexão com o banco de dados mysql

# Inicializando conexão com o mariaDB

connnection = criarConexao(
    endereco="localhost", usuario="monty", senha="admin", bancodedados="teste"
)

# Inserindo dados no banco de dados

sql = f"INSERT INTO filmes (titulo, ano, genero) VALUES ({'Titanic'}, {1997}, {'Romance'})"

id = insertNoBancoDados(connnection, sql)

print(f"ID do filme inserido: {id}")

encerrarConexao(connnection)
