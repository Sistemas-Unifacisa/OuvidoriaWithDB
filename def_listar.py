from operacoesbd import listarBancoDados, encerrarConexao

# Lucas Arruda -

def listar_manifestacoes(conexao):
    menu = "1. Elogios\n2. Reclamações\n3. Sugestões\n4. Voltar\nEscolha uma opção: "
    while True:
        try:
            opcao = int(input(menu))
            if opcao == 1:
                listar_Elogios(conexao)
            elif opcao == 2:
                listar_Reclamacoes(conexao)
            elif opcao == 3:
                listar_Sugestoes(conexao)
            elif opcao == 4:
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            
def listar_Elogios(conexao):
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
        print(f"Código: {elogios[0]}, Descrição: {elogios[1]}")


def listar_Reclamacoes(conexao):
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
        print(f"Código: {reclamacoes[0]}, Descrição: {reclamacoes[1]}")


def listar_Sugestoes(conexao):
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
        print(f"Código: {sugestoes[0]}, Descrição: {sugestoes[1]}")
