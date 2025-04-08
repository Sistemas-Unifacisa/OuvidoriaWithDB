# 1. Criar menu para decidir qual categoria de manifestação, (Elogio, Reclamação ou Sugestão)
from connection import get_connection
from operacoesbd import listarBancoDados  # Importa a função para buscar registros no banco de dados

def exibir_menu_categoria():
    print("Qual categoria você deseja ver? ")
    print("1. Elogio")
    print("2. Reclamação")
    print("3. Sugestão")
    
    while True:
        try:
            opcao = int(input("Digite o número correspondente à categoria desejada: "))
            if opcao in [1, 2, 3]:
                categorias = {1: "Elogio", 2: "Reclamação", 3: "Sugestão"}
                print(f"Você selecionou: {categorias[opcao]}")
                return categorias[opcao]
            else:
                print("Opção inválida. Por favor, escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def buscar_por_categoria(categoria):
    # Cria a consulta SQL para buscar registros da categoria
    sql = f"SELECT id, descricao FROM manifestacoes WHERE categoria = '{categoria}'"
    
    # Chama a função do módulo `operacoes_bd` para buscar registros no banco de dados
    registros = listarBancoDados(sql)
    
    if registros:
        print(f"\nRegistros encontrados para a categoria '{categoria}':")
        for registro in registros:
            print(f"ID: {registro['id']}, Descrição: {registro['descricao']}")
    else:
        print(f"\nNenhum registro encontrado para a categoria '{categoria}'.")

if __name__ == "__main__":
    # Exibe o menu e obtém a categoria selecionada
    categoria_selecionada = exibir_menu_categoria()
    
    # Busca e exibe os registros da categoria selecionada
    buscar_por_categoria(categoria_selecionada)
# 2. Criar um input informando qual o código para pesquisar (int)
# 3. Realizar conexão na tabela escolhida

