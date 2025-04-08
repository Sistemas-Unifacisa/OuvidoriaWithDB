from connection import get_connection
from operacoesbd import excluirBancoDados, listarBancoDados

def selecionar_tipo_manifestacao_para_exclusao():
    """
    Função que escolhe o tipo de manifestação a ser excluída.
    """

    tabelas = ["Reclamacao", "Elogio", "Sugestao"]
    
    print("\nINFO: Opcões disponíveis:\n1) Remover Reclamação\n2) Remover Elogio\n3) Remover Sugestões")

    try:
        resposta = int(input("\n> Escolha uma categoria: "))

        if resposta not in [1, 2, 3]:
            print("\nINFO: Opção inválida.")
            return

    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    excluirCodigo = int(input("\n> Digite o código da manifestação que deseja excluir: "))
    excluir_manifestacao(excluirCodigo, tabelas[resposta - 1])


def excluir_manifestacao(excluirCodigo, tabela):
    """
    Função que exclui a manifestação do banco de dados.
    """

    conexao = get_connection()

    if not exibir_manifestacao_para_exclusao(conexao, tabela, excluirCodigo):
        print("\nINFO: Nenhuma manifestação encontrada com esse código.")
        return

    confirmacao = input("\n> Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmacao == "s":
        consulta = f"DELETE FROM Manifestacao WHERE id = {excluirCodigo} AND tipo = '{tabela}'"
        linhasModificadas = excluirBancoDados(conexao, consulta)

        if linhasModificadas == 0:
            print("\nINFO: Nenhuma manifestação encontrada com esse código.")
        else:
            print("\nINFO: Manifestação excluída com sucesso.")

    elif confirmacao == "n":
        print("\nINFO: Operação cancelada.")
    else:
        print("\nINFO: Opção inválida. DIGITE APENAS : (S/N)")


def exibir_manifestacao_para_exclusao(connection, tabela, excluirCodigo):
    """
    Função que exibe a manifestação que será excluída.    
    """

    sql = f"SELECT * FROM Manifestacao WHERE id = {excluirCodigo} AND tipo = '{tabela}'"
    manifestacao = listarBancoDados(connection, sql)

    if manifestacao:
        print(f"\nCódigo: {manifestacao[0][0]}")
        print(f"\nDescrição: {manifestacao[0][1]}")
        return True

    return False
