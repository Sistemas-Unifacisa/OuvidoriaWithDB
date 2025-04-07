from tabelas import Reclamacao, Elogio, Sugestao


def adicionar_manifestacao():
    """
    Função para adicionar uma nova manifestação (reclamação, elogio ou sugestão) ao banco de dados.
    """

    print("\nINFO: Opcões disponíveis:")
    print("1) Adicionar Reclamação")
    print("2) Adicionar Elogio")
    print("3) Adicionar Sugestões")

    resposta = int(input("\n> Escolha uma categoria: "))

    if resposta == 1:
        descricao = input("\n> Digite a sua reclamação: ").strip()

        if len(descricao) == 0:
            print("\nErro: Campo vazio!")
            return

        reclamacao = Reclamacao(descricao=descricao)
        resultado = reclamacao.inserir()

        if resultado:
            print(f"\nINFO: Reclamação com código {resultado} registrada com sucesso!")
            return

        print("\nERRO: Erro ao registrar a reclamação.")

    elif resposta == 2:
        descricao = input("\nDigite o seu elogio: ")

        if len(descricao) == 0:
            print("\nErro: Campo vazio!")
            return

        elogio = Elogio(descricao=descricao)
        resultado = elogio.inserir()

        if resultado:
            print(f"\nINFO: Elogio com código {resultado} registrado com sucesso!")
        else:
            print("\nERRO: Erro ao registrar a elogio.")

    elif resposta == 3:
        descricao = input("\nDigite a sua Sugestão:\n")

        if len(descricao) == 0:
            print("Erro! Campo vazio")
            return

        sugestao = Sugestao(descricao=descricao)
        resultado = sugestao.inserir()

        if resultado:
            print(f"\nINFO: Sugestão com código {resultado} registrada com sucesso!")
            return

        print("\nERRO: Erro ao registrar a sugestão.")

    else:
        print("\nERRO: Categoria não encontrada!")
