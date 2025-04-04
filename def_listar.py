from operacoesbd import listarBancoDados, encerrarConexao

def listar_manifestacoes(conn):
    sql = "SELECT * FROM manifestacao"  # definir em uma variavel o que eu quero passar pro SQL
    manifestações = listarBancoDados(conn, sql)
    # com os paranmentros definidos, enviamos pro BANCO DE DADOS e ele vai ler o (sql) que eu coloquei a str do que eu quero colocar no MYSQL

    if manifestações == 0:
        print("Nenhuma manifestação cadastrada")
    else:
        print(f'Aqui estão as manifestações cadastradas:')
        for n in range(len(manifestações)):
            print(f"{n + 1} - {manifestações[n]}")

    encerrarConexao(conn)


"""  Tratamentos Necessários: 
• Ao listar, caso não tenha nenhuma manifestação, informar ao usuário que não 
existem manifestações cadastradas 
• Ao listar, exibir o número da manifestação e a data de abertura da manifestação"""
