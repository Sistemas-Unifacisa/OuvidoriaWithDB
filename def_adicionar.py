from tabelas import Reclamacao


def adicionar_manifestacao():
    print("1) Adicionar Reclamação")
    print("2) Adicionar Elogio")
    print("3) Adicionar Sugestões")
    resposta = int(input("\nEscolha uma categoria :\n"))

    if resposta == 1:
        descricao = str(input("\nDigite a sua reclamação:\n")).strip()

        if len(descricao) == 0:
            print("Erro! Campo vazio")

        else:
            reclamacao = Reclamacao(descricao=descricao)
            reclamacao.inserir()

            if reclamacao:
                print("Reclamação registrada com sucesso!")
            else:
                print("Erro ao registrar a reclamação.")

    elif resposta == 2:
        descricao = input("\nDigite o seu elogio:\n")
        if len(descricao) == 0:
            print("Erro! Campo vazio")
        else:
            print("Elogio registrado com sucesso!")

    elif resposta == 3:
        descricao = input("\nDigite a sua Sugestão:\n")
        if len(descricao) == 0:
            print("Erro! Campo vazio")
        else:
            print("Sugestão registrada com sucesso!")
    else:
        print("Erro! Categoria não encontrada")


""" consultainserir = f"insert into Ouvidoria(titulo, sinopse, ano) values({titulo_filme},{sinopse_filme},{ano_filme})"""
