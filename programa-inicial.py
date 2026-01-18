#Ideia é ser um cadastro que te dê opções de escolher gerar uma senha ou criar uma sua.#

# Menu Inicial
while True:
    print("MENU INICIAL")
    print("Digite '1' para abrir o programa")
    print("Digite '2' para sair do programa")
    print("Digite 'pare' para parar o programa")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("Programa aberto com sucesso, seja bem-vindo! Esse programa serve para guardar anotações pequenas, como uma espécie de lembrete.")
        
        # Aqui deve ser colocado o código do programa

    elif opcao == "2":
        print("Saindo do programa...")
        break

    else: 
        print("Opção inválida, tente novamente!")