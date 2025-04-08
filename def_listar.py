from operacoesbd import listarBancoDados
from connection import get_connection

tipos = ["Reclamacao", "Elogio", "Sugestao"]


def listar_manifestacoes():
    """
    Função para listar todas as manifestações (elogios, reclamações e sugestões) do banco de dados.
    """

    listar_manifestacao(tipos[0])
    listar_manifestacao(tipos[1])
    listar_manifestacao(tipos[2])
    print("")


def listar_manifestacoes_por_tipo():
    """
    Função para listar manifestações por tipo (elogios, reclamações e sugestões).
    """

    while True:
        try:  # Tratativa de erro para entradas inválidas
            opcao = int(input(
                "\n1. Listar Elogios\n2. Listar Reclamações\n3. Listar Sugestões\n4. Voltar para o menu\n\n> Escolha uma opção: "))

            if opcao == 1:
                listar_manifestacao(tipos[1])
                break
            elif opcao == 2:
                listar_manifestacao(tipos[0])
                break
            elif opcao == 3:
                listar_manifestacao(tipos[2])
                break
            elif opcao == 4:
                print("\nINFO: Voltando ao menu principal...\n")
                break
            else:
                print("\nINFO: Opção inválida. Tente novamente.")

        except ValueError:
            print("\nERRO: Entrada inválida. Por favor, insira um número.")


def listar_manifestacao(tipo_manifestacao):
    """
    Função para listar uma manifestação específica (elogio, reclamação ou sugestão) por código.
    """

    conexao = get_connection()

    sql = f"SELECT * FROM Manifestacao WHERE tipo = '{tipo_manifestacao}'"

    manifestacoes = listarBancoDados(conexao, sql)

    if not manifestacoes:
        print(
            f"\nINFO: Nenhuma manifestação do tipo {tipo_manifestacao} encontrada.")
        return

    print(f"\nINFO: Manifestações do tipo {tipo_manifestacao} encontradas:")

    for manifestacao in manifestacoes:
        print(f"Código: {manifestacao[0]}, Descrição: {manifestacao[1]}")

    conexao.close()
