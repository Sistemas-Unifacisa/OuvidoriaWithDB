from operacoesbd import listarBancoDados


def listar_filmes(conn):
    sql = (
        "SELECT * FROM filmes"  # definir em uma variavel o que eu quero passar pro SQL
    )

    lista_de_Filmes = listarBancoDados(conn, sql)
    # com os paranmentros definidos, enviamos pro BANCO DE DADOS e ele vai ler o (sql) que eu coloquei a str do que eu quero colocar no MYSQL

    print(f"{lista_de_Filmes}")  # inporta do banco e retorna num print
