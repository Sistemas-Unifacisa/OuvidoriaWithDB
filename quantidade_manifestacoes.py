from connection import get_connection
from operacoesbd import listarBancoDados


def mostrar_quantidade_manifestacoes():
    """
    Função para mostrar a quantidade de manifestações cadastradas no banco de dados.
    """

    # Conectar ao banco de dados
    conexao = get_connection()

    sql_sugestoes = "SELECT COUNT(*) FROM Sugestao"
    sql_reclamacoes = "SELECT COUNT(*) FROM Reclamacao"
    sql_elogios = "SELECT COUNT(*) FROM Elogio"

    # Executar as consultas
    sugestoes = listarBancoDados(conexao, sql_sugestoes)
    reclamacoes = listarBancoDados(conexao, sql_reclamacoes)
    elogios = listarBancoDados(conexao, sql_elogios)

    # Fechar a conexão
    conexao.close()

    # Exibir os resultados
    print("\nINFO: Quantidade de manifestações cadastradas:")
    print(f"1) Reclamações: {reclamacoes[0][0]}")
    print(f"2) Elogios: {elogios[0][0]}")
    print(f"3) Sugestões: {sugestoes[0][0]}")
    print(
        f"4) Total de manifestações: {sugestoes[0][0] + reclamacoes[0][0] + elogios[0][0]}\n")
