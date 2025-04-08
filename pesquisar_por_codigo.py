from operacoesbd import listarBancoDados
from connection import get_connection

tabelas = ["Reclamacao", "Elogio", "Sugestao"]


def pesquisar_manifestacao_por_codigo():
    """
    Função principal para pequisar uma manifestação por código.
    """

    categoria_selecionada = exibir_menu_categoria()
    codigo_manifestacao = get_codigo_manifestacao()

    buscar_por_categoria(
        categoria_selecionada, tabelas[categoria_selecionada - 1], codigo_manifestacao)


def exibir_menu_categoria():
    """
    Função que exibe o menu de categorias e retorna a opção escolhida pelo usuário.
    """

    print("\nINFO: Qual categoria você deseja ver? ")
    print("1. Reclamação")
    print("2. Elogio")
    print("3. Sugestão")

    while True:
        try:
            opcao = int(
                input("\n> Digite o número correspondente à categoria desejada: "))

            if opcao in [1, 2, 3]:
                print(f"\nINFO: Você selecionou: {tabelas[opcao - 1]}")
                return opcao
            else:
                print("\nERRO: Opção inválida. Por favor, escolha entre 1, 2 ou 3.")

        except ValueError:
            print("\nERRO: Opção inválida. Por favor, insira um número.")


def buscar_por_categoria(categoria, tabela, codigo):
    """
    Função que busca registros no banco de dados com base na categoria e código fornecidos.
    """

    connection = get_connection()

    # Cria a consulta SQL para buscar registros da categoria
    sql = f"SELECT * FROM Manifestacao WHERE id = {codigo} AND tipo = '{tabela}'"

    # Chama a função do módulo `operacoes_bd` para buscar registros no banco de dados
    registros = listarBancoDados(connection, sql)

    if registros:
        print(f"\nINFO: Registros encontrados para a categoria '{categoria}':")

        for registro in registros:
            print(f"ID: {registro[0]}, Descrição: {registro[1]}\n")
    else:
        print(
            f"\nINFO: Nenhum registro encontrado para a categoria '{categoria}'.\n")


def get_codigo_manifestacao():
    """
    Função que solicita ao usuário o código da manifestação e valida a entrada.
    """

    while True:
        try:
            codigo = int(input("\n> Digite o código da manifestação: "))
            return codigo

        except ValueError:
            print("\nERRO: Código inválido. Por favor, insira um número inteiro.")
