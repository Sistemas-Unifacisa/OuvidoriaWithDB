"""
Lucas Arruda - Mostrar Filmes Removidos ( feito )
Carlos Lopes - Revisar a bagaça toda (faz porra nenhuma)
Georgio Filho - Adicionar Filmes (feito )
Ryan Matheus - Remover Filmes (Não sou vagabundo - Feito)
"""

from def_listar import listar_manifestacoes_por_tipo, listar_manifestacoes
from operacoesbd import criarConexao, encerrarConexao
from def_adicionar import adicionar_manifestacao
from mostrar_menu import mostrar_menu
from create_tables import load_database_config
from def_remover import excluir_manifestacao
from quantidade_manifestacoes import mostrar_quantidade_manifestacoes

load_database_config()

while True:
    mostrar_menu()

    opcao = int(input("> Escolha uma opção: "))

    if opcao == 1:  # Listagem das Manifestações
        listar_manifestacoes()
    elif opcao == 2:  # Listagem de Manifestações por Tipo
        listar_manifestacoes_por_tipo()
        ...
    elif opcao == 3:  # Criar uma nova Manifestação
        adicionar_manifestacao()
    elif opcao == 4:  # Exibir quantidade de manifestações
        mostrar_quantidade_manifestacoes()
    elif opcao == 5:  # Pesquisar uma manifestação por código
        ...
    elif opcao == 6:  # Excluir uma Manifestação pelo Código
        excluir_manifestacao()
    elif opcao == 7:  # Sair do Sistema
        break
    else:
        print("Opção inválida. Tente novamente.")
        ...
print("\nINFO: A ouvidoria agradece sua participação !")
