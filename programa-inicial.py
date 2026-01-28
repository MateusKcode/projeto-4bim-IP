import string
import random
from gerador import gerador_senhas

# Lista onde serão armazenados os cadastros (referência + senha)
cadastros = []

# Lista onde serão armazenados os lembretes (referência + lembrete)
lembretes = []

# ================= MENU INICIAL =================
while True:
    text = """

██████████████████████████████████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄███▄─▄█▄─▀█▄─▄█▄─▄█─▄▄▄─█▄─▄██▀▄─██▄─▄███
██─█▄█─███─▄█▀██─█▄▀─███─██─█████─███─█▄▀─███─██─███▀██─███─▀─███─██▀█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
"""
    print(text)
    print("Digite '1' para abrir o programa")
    print("Digite '2' para sair do programa")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        text3 = """
Pʀᴏɢʀᴀᴍᴀ ᴀʙᴇʀᴛᴏ ᴄᴏᴍ sᴜᴄᴇssᴏ!
"""
        print(text3)

        # ============== MENU PRINCIPAL ==============
        while True:
            text2 = """

█▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀█ █ █▄░█ █▀▀ █ █▀█ ▄▀█ █░░
█░▀░█ ██▄ █░▀█ █▄█   █▀▀ █▀▄ █ █░▀█ █▄▄ █ █▀▀ █▀█ █▄▄
            """
            print(text2)
            print("1 - Gerar senha")
            print("2 - Entrar com senha gerada ou própria")
            print("3 - Ver cadastros")
            print("4 - Criar lembrete")
            print("5 - Ver lembretes")
            print("6 - Voltar")

            escolha = input("Digite uma opção: ")

            # Gerar senha automática
            if escolha == "1":
                senha = gerador_senhas(8)
                print(f"Sua senha gerada é: {senha}")

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
                text4 = """
Vᴏʟᴛᴀɴᴅᴏ ᴀᴏ ᴍᴇɴᴜ ɪɴɪᴄɪᴀʟ..."""
                print(text4)
                break

            else:
                print("Opção inválida!")

    elif opcao == "2":
        text5 = """
sᴀɪɴᴅᴏ ᴅᴏ ᴘʀᴏɢʀᴀᴍᴀ...
"""
        print(text5)
        break

    else:
        print("Opção inválida, tente novamente!")
