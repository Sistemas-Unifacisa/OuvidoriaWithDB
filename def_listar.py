from operacoesbd import listarBancoDados


def listar_manifestações(conn):
    sql = (
        "SELECT * FROM manifestacao"  # definir em uma variavel o que eu quero passar pro SQL
    )

    listar_manifestações = listarBancoDados(conn, sql)
    # com os paranmentros definidos, enviamos pro BANCO DE DADOS e ele vai ler o (sql) que eu coloquei a str do que eu quero colocar no MYSQL

    print(f"{listar_manifestações}")  # inporta do banco e retorna num print
