from operacoesbd import listarBancoDados, encerrarConexao
from connection import get_connection


def listar_manifestacoes():
    listar_Elogios()
    listar_Sugestoes()
    listar_Reclamacoes()


def listar_manifestacoes_por_tipo():
    menu = "1. Elogios\n2. Reclamações\n3. Sugestões\n4. Voltar\nEscolha uma opção:"
    while True:
        try:
            opcao = int(input(menu))
            if opcao == 1:
                listar_Elogios()
            elif opcao == 2:
                listar_Reclamacoes()
            elif opcao == 3:
                listar_Sugestoes()
            elif opcao == 4:
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def listar_Elogios():
    conexao = get_connection()

    # Consulta SQL para selecionar todas as manifestações do tipo 'Elogio'
    sql = "SELECT * FROM Elogio"

    # Verifica se existem manifestações do tipo 'Elogio'
    elogios = listarBancoDados(conexao, sql)

    if not elogios:
        print("Nenhum elogio encontrado.")
        return

    # Imprime as manifestações do tipo 'Elogio' encontradas
    print("Elogios encontrados:")
    for elogio in elogios:
        print(f"Código: {elogio[0]}, Descrição: {elogio[1]}")

    conexao.close()


def listar_Reclamacoes():
    conexao = get_connection()

    # Consulta SQL para selecionar todas as manifestações do tipo 'Reclamacao'
    sql = "SELECT * FROM Reclamacao"

    # Verifica se existem manifestações do tipo 'Reclamacao'
    reclamacoes = listarBancoDados(conexao, sql)

    if not reclamacoes:
        print("Nenhuma reclamação encontrada.")
        return

    # Imprime as manifestações do tipo 'Reclamacao' encontradas
    print("Reclamações encontradas:")
    for reclamacao in reclamacoes:
        print(f"Código: {reclamacao[0]}, Descrição: {reclamacao[1]}")

    conexao.close()


def listar_Sugestoes():
    conexao = get_connection()
    # Consulta SQL para selecionar todas as manifestações do tipo 'Sugestao'
    sql = "SELECT * FROM Sugestao"

    # Verifica se existem manifestações do tipo 'Sugestao'
    sugestoes = listarBancoDados(conexao, sql)

    if not sugestoes:
        print("Nenhuma sugestão encontrada.")
        return

    # Imprime as manifestações do tipo 'Sugestao' encontradas
    print("Sugestões encontradas:")
    for sugestao in sugestoes:
        print(f"Código: {sugestao[0]}, Descrição: {sugestao[1]}")
    conexao.close()
