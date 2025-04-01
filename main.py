"""
Lucas Arruda - Mostrar Filmes Removidos ( feito )
Carlos Lopes - Revisar a bagaça toda (faz porra nenhuma)
Georgio Filho - Adicionar Filmes (feito )
Ryan - Remover Filmes (FEZ PORRA NENHUMA)
"""

from def_listar import listar_filmes
from operacoesbd import criarConexao, encerrarConexao
from def_adicionar import adicionarFilme
from mostrar_menu import mostrar_menu
from opcoes import LISTAR, ADICIONAR, REMOVER, MOSTRAR_LOCADOS, EDITAR, SAIR

connection = criarConexao(
    endereco="localhost", usuario="monty", senha="admin", bancodedados="teste"
)
while True:
    mostrar_menu()

    opcao = int(input("> Escolha uma opção: "))

    if opcao == LISTAR:  # listar filmes
        listar_filmes(connection)

    elif opcao == ADICIONAR:  # adicionar Filme
        adicionarFilme(connection)

    elif opcao == REMOVER:  # Remover Filmes
        ...

    elif opcao == MOSTRAR_LOCADOS:  # Remover Filmes
        ...
    elif opcao == EDITAR:  # Editar informações do filme ( fazer todos juntos )
        ...
    elif opcao == SAIR:
        break
        ...
    else:
        print("ERRO: Opção invalida!")

print("INFO: A locadora agradece sua participação ")
encerrarConexao(connection)
