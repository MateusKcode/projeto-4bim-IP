import string
import random

# Lista onde serão armazenados os cadastros (referência + senha)
cadastros = []

# Lista onde serão armazenados os lembretes (referência + lembrete)
lembretes = []

# Função responsável por gerar senhas aleatórias
def gerador_senhas(comprimento):
    chars = string.ascii_letters + string.digits + string.punctuation
    senha = []
    for i in range(comprimento):
        senha.append(random.choice(chars))
    return ''.join(senha)

# ================= MENU INICIAL =================
while True:
    print("\nMENU INICIAL")
    print("Digite '1' para abrir o programa")
    print("Digite '2' para sair do programa")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("\nPrograma aberto com sucesso!")

        # ============== MENU PRINCIPAL ==============
        while True:
            print("\nMENU PRINCIPAL")
            print("1 - Gerar senha")
            print("2 - Entrar com senha gerada ou própria")
            print("3 - Ver cadastros")
            print("4 - Criar lembrete")
            print("5 - Ver lembretes")
            print("6 - Voltar")

            escolha = input("Digite uma opção: ")

            # Gerar senha automática
            if escolha == "1":
                referencia = input("Digite uma referência: ")
                senha = gerador_senhas(8)
                cadastros.append((referencia, senha))
                print("Senha gerada:", senha)

            # Usar senha própria
            elif escolha == "2":
                referencia = input("Digite seu usuário: ")
                senha = input("Digite sua senha: ")
                cadastros.append((referencia, senha))
                print("Senha salva com sucesso!")

            # Ver cadastros
            elif escolha == "3":
                if not cadastros:
                    print("Nenhum cadastro ainda.")
                else:
                    for ref, senha in cadastros:
                        print(ref, "-", senha)

            # Criar lembrete
            elif escolha == "4":
                referencia = input("Digite o nome do lembrete: ")
                texto = input("Digite o lembrete: ")
                lembretes.append((referencia, texto))
                print("Lembrete salvo com sucesso!")

            # Ver lembretes
            elif escolha == "5":
                if not lembretes:
                    print("Nenhum lembrete salvo.")
                else:
                    for ref, texto in lembretes:
                        print(ref, "→", texto)

            # Voltar ao menu inicial
            elif escolha == "6":
                print("Voltando ao menu inicial...")
                break

            else:
                print("Opção inválida!")

    elif opcao == "2":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente!")
