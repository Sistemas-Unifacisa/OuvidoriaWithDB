from operacoesbd import insertNoBancoDados


def adicionarManifestação(connection):

    print("1) Reclamação")
    print("2) Elogio")
    print("3) Sugestões")
    resposta = int(input('\nEscolha uma categoria :\n'))

    if resposta == 1:
        descricao = input('\nDigite a sua reclamação:\n')
    elif resposta == 2:
        descricao = input('\nDigite o seu elogio:\n')
    elif resposta == 3:
        descricao = input('\nDigite a sua Sugestão:\n')
    else:
        print('Erro! Categoria não encontrada')


""" consultainserir = f"insert into Ouvidoria(titulo, sinopse, ano) values({titulo_filme},{sinopse_filme},{ano_filme})"""


print("Nova manifestação inserida, com sucesso!")
