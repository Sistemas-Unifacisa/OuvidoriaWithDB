from connection import get_connection
from operacoesbd import excluirBancoDados, listarBancoDados

# TODO: Deixar o código mais limpo e organizado.


def excluir_manifestacao():
    """
    Função para excluir uma manifestão do banco de dados.
    """

    print("\nINFO: Opcões disponíveis:")
    print("1) Remover Reclamação")
    print("2) Remover Elogio")
    print("3) Remover Sugestões")

    tabelas = ["Reclamacao", "Elogio", "Sugestao"]
    resposta = int(input("\n> Escolha uma categoria: "))

    excluirCodigo = int(
        input("\n> Digite o código da manifestação que deseja excluir: ")
    )

    if resposta == 1:
        excluir_entidade(excluirCodigo, tabelas[0])
    elif resposta == 2:
        excluir_entidade(excluirCodigo, tabelas[1])
    elif resposta == 3:
        excluir_entidade(excluirCodigo, tabelas[2])


def excluir_entidade(excluirCodigo, tabela):
    while True:
        conexao = get_connection()

        existe_manifestacao = mostrar_manifestacao_pra_ser_deletada(
            conexao, tabela, excluirCodigo
        )

        if not existe_manifestacao:
            print("\nINFO: Nenhuma manifestação encontrada com esse código.")
            break

        confirmacao = input("\n> Tem certeza que deseja excluir? (s/n): ")

        if confirmacao.lower() == "s":
            consulta = f"DELETE FROM {tabela} WHERE id = {excluirCodigo}"

            linhasModificadas = excluirBancoDados(conexao, consulta)

            if linhasModificadas == 0:
                print("\nINFO: Nenhuma manifestação encontrada com esse código.")
            else:
                print("\nINFO: Manifestação excluída com sucesso.")
            break  # Encerra o loop após a tentativa

        elif confirmacao.lower() == "n":
            print("Operação cancelada.")
            break

        else:
            print("Opção inválida. DIGITE APENAS : (S/N)")


def mostrar_manifestacao_pra_ser_deletada(connection, tabela, excluirCodigo):
    sql = f"SELECT * FROM {tabela} WHERE id = {excluirCodigo}"
    manifestacao = listarBancoDados(connection, sql)

    if manifestacao:
        print(f"\nCódigo: {manifestacao[0][0]}")
        print(f"\nDescrição: {manifestacao[0][1]}")

        return True

    return False
