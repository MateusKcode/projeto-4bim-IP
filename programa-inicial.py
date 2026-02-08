import string
import random
import json
import os
from gerador import gerador_senhas

# Nome do arquivo JSON
ARQUIVO = "dados.json"

# ================= FUNÇÕES JSON =================

def carregar_dados():
    """Carrega os dados salvos no arquivo JSON."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"cadastros": [], "lembretes": []}


def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


# ================= INÍCIO DO PROGRAMA =================

# Carrega os dados salvos ao iniciar
dados = carregar_dados()

# Listas principais
cadastros = dados["cadastros"]
lembretes = dados["lembretes"]

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

            # Criar cadastro
            elif escolha == "2":
                referencia = input("Digite seu usuário: ")
                senha = input("Digite sua senha: ")

                cadastros.append({"usuario": referencia, "senha": senha})
                salvar_dados(dados)

                print("Senha salva com sucesso!")

            # Ver cadastros
            elif escolha == "3":
                if not cadastros:
                    print("Nenhum cadastro ainda.")
                else:
                    print("\nCADASTROS SALVOS:")
                    for c in cadastros:
                        print(c["usuario"], "-", c["senha"])

            # Criar lembrete
            elif escolha == "4":
                referencia = input("Digite o nome do lembrete: ")
                texto = input("Digite o lembrete: ")

                lembretes.append({"titulo": referencia, "texto": texto})
                salvar_dados(dados)

                print("Lembrete salvo com sucesso!")

            # Ver lembretes
            elif escolha == "5":
                if not lembretes:
                    print("Nenhum lembrete salvo.")
                else:
                    print("\nLEMBRETES SALVOS:")
                    for l in lembretes:
                        print(l["titulo"], "→", l["texto"])

            # Voltar
            elif escolha == "6":
                text4 = """
Vᴏʟᴛᴀɴᴅᴏ ᴀᴏ ᴍᴇɴᴜ ɪɴɪᴄɪᴀʟ...
"""
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
