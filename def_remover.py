from operacoesbd import *
#Ryan M
def excluir_manifestacao():
    
    # Conexão com o banco de dados
    conex = criarConexao('127.0.0.1', 'root', '12345', 'ouvidoria')

    excluirCodigo = int(input("Digite o código da manifestação que deseja excluir: "))
    # Pede para o usuário digitar o ID da manifestação que o usuário quer excluir.

    while True:
        confirmacao = input("Tem certeza que deseja excluir? (s/n): ")
        # Confirma com o usuário se ele confirma a exclusão da manifestação.

        if confirmacao.lower() == "s":
            consulta = "DELETE FROM manifestacao WHERE id = %s"
            dados = [excluirCodigo]
            # Verifica se o usuário digitou "s" (minúsculo ou maiúsculo)
            # Se sim, exclui a manifestação. Caso contrário, cancela a operação.

            linhasModificadas = excluirBancoDados(conex, consulta, dados)

            if linhasModificadas == 0:
                print("Nenhuma manifestação encontrada com esse código.")
            else:
                print("Manifestação excluída com sucesso.")
            break  # Encerra o loop após a tentativa
        elif confirmacao.lower() == "n":
            print("Operação cancelada.")
            break # encerra o loop depois da tentativa
        else:
            print("Opção inválida. DIGITE APENAS : (S/N)")

    encerrarConexao(conex)



