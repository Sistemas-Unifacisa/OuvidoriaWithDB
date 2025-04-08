# Importa as classes Reclamacao, Elogio e Sugestao do módulo 'tabelas'
from tabelas import Reclamacao, Elogio, Sugestao

# Define a função principal para adicionar uma manifestação (reclamação, elogio ou sugestão)


def adicionar_manifestacao():

 # Exibe as opções disponíveis para o usuário
    print("\nINFO: Opcões disponíveis:")
    print("1) Adicionar Reclamação")
    print("2) Adicionar Elogio")
    print("3) Adicionar Sugestões")

# Solicita que o usuário escolha uma das opções
    resposta = int(input("\n> Escolha uma categoria: "))

    # Caso a opção escolhida seja Reclamação
    if resposta == 1:
        descricao = input("\n> Digite a sua reclamação: ").strip()

        # Verifica se a descrição está vazia
        if len(descricao) == 0:
            print("\nErro: Campo vazio!")
            return

        # Cria um objeto da classe Reclamacao e insere no banco
        reclamacao = Reclamacao(descricao=descricao)
        resultado = reclamacao.inserir()

        if resultado:
            print(
                f"\nINFO: Reclamação com código {resultado} registrada com sucesso!")
            return

        print("\nERRO: Erro ao registrar a reclamação.")

    # Caso a opção escolhida seja Elogio
    elif resposta == 2:
        descricao = input("\nDigite o seu elogio: ")

        if len(descricao) == 0:
            print("\nErro: Campo vazio!")
            return

        elogio = Elogio(descricao=descricao)
        resultado = elogio.inserir()

        if resultado:
            print(
                f"\nINFO: Elogio com código {resultado} registrado com sucesso!")
        else:
            print("\nERRO: Erro ao registrar a elogio.")

    # Caso a opção escolhida seja Sugestão
    elif resposta == 3:
        descricao = input("\nDigite a sua Sugestão:\n")

        if len(descricao) == 0:
            print("Erro! Campo vazio")
            return

        sugestao = Sugestao(descricao=descricao)
        resultado = sugestao.inserir()

        if resultado:
            print(
                f"\nINFO: Sugestão com código {resultado} registrada com sucesso!")
            return

        print("\nERRO: Erro ao registrar a sugestão.")

    # Caso o usuário tenha escolhido uma opção inválida
    else:
        print("\nERRO: Categoria não encontrada!")
