from operacoesbd import insertNoBancoDados


def adicionarFilme(connection):
    titulo_filme = input("Digite o titulo do novo filme: ")
    sinopse_filme = input("Digite a sinopse do novo filme: ")
    ano_filme = int(input("Digite o ano do novo filme: "))

    consultainserir = f"insert into filmes(titulo, sinopse, ano) values({titulo_filme},{sinopse_filme},{ano_filme})"

    insertNoBancoDados(connection, consultainserir)
    print("Filme inserido com sucesso!")


# Outra forma de fazer, utilizando %s

"""consultainserir = "insert into filmes(titulo, sinopse, ano) values(%s,%s,%s)"  
    dados = (titulo_filme, sinopse_filme, ano_filme)

    insertNoBancoDados(connection, consultainserir, dados)
    print("Filme inserido com sucesso!")"""


"""' %s não necessariamente precisa ser usado nos valores pois
podemos passar os valores direto no segundo paramêtro sem precisar ficar 'devendo' nada."""
