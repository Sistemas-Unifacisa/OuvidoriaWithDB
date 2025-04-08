"""
Lucas Arruda
Carlos Lopes
Georgio Filho
Ryan Matheus
Thiago Oliveira
"""

from def_listar import listar_manifestacoes_por_tipo, listar_manifestacoes
from def_adicionar import adicionar_manifestacao
from def_remover import selecionar_tipo_manifestacao_para_exclusao
from pesquisar_por_codigo import pesquisar_manifestacao_por_codigo
from quantidade_manifestacoes import mostrar_quantidade_manifestacoes
from connection import load_database_config

load_database_config()

while True:
    print("*" * 30)
    print("    Bem-vindo a Ouvidoria!    ")
    print("*" * 30)

    print("""
    ---------- Opções ----------
• 1) Listagem das Manifestações 
• 2) Listagem de Manifestações por Tipo 
• 3) Criar uma nova Manifestação  
• 4) Exibir quantidade de manifestações  
• 5) Pesquisar uma manifestação por código 
• 6) Excluir uma Manifestação pelo Código 
• 7) Sair do Sistema. 
    ----------------------""")
    try:
        opcao = int(input("> Escolha uma opção: "))

        if opcao == 1:  # Listagem das Manifestações
            listar_manifestacoes()
        elif opcao == 2:  # Listagem de Manifestações por Tipo
            listar_manifestacoes_por_tipo()
        elif opcao == 3:  # Criar uma nova Manifestação
            adicionar_manifestacao()
        elif opcao == 4:  # Exibir quantidade de manifestações
            mostrar_quantidade_manifestacoes()
        elif opcao == 5:  # Pesquisar uma manifestação por código
            pesquisar_manifestacao_por_codigo()
        elif opcao == 6:  # Excluir uma Manifestação pelo Código
            selecionar_tipo_manifestacao_para_exclusao()
        elif opcao == 7:  # Sair do Sistema

            break
        else:
            print("\nERRO: Opção inválida. Tente novamente.")

        input("Pressione qualquer tecla para continuar...")

    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, insira um número.\n")

print("\nINFO: A ouvidoria agradece sua participação !")
