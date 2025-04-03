"""
Lucas Arruda - Mostrar Filmes Removidos ( feito )
Carlos Lopes - Revisar a bagaça toda (faz porra nenhuma)
Georgio Filho - Adicionar Filmes (feito )
Ryan - Remover Filmes (FEZ PORRA NENHUMA)
"""

from def_listar import listar_manifestacoes
from operacoesbd import criarConexao, encerrarConexao
from def_adicionar import adicionar_manifestacao
from mostrar_menu import mostrar_menu

# TODO: Solicitar login com nome do usuário para registro no sistema.

while True:
    mostrar_menu()

    opcao = int(input("> Escolha uma opção: "))

    if opcao == 1:  # Listagem das Manifestações
        ...
    elif opcao == 2:  # Listagem de Manifestações por Tipo
        ...
    elif opcao == 3:  # Criar uma nova Manifestação
        adicionar_manifestacao()
    elif opcao == 4:  # Exibir quantidade de manifestações
        ...
    elif opcao == 5:  # Pesquisar uma manifestação por código
        ...
    elif opcao == 6:  # Excluir uma Manifestação pelo Código
        ...
    elif opcao == 7:  # Sair do Sistema
        break
    else:
        print("Opção inválida. Tente novamente.")
        ...
print("INFO: A locadora agradece sua participação ")
