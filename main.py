import os
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_anotacao():
    with open("anotação.txt", "a") as file:
            file.write(input("Anotação... ") + "\n")
            print("Anotação salva com sucesso.")
            input("Pressione Enter para continuar...")
            limpar_tela()

def ler_anotacao():
    try:
         with open("anotação.txt", "r") as file:
                conteudo = file.read()
                if conteudo.strip() == "":
                    print("Nenhuma anotação encontrada.")
                else:
                    print(conteudo)
    except FileNotFoundError:
            print("Nenhuma anotação encontrada.")

def excluir_anotacao():
    try:
            with open("anotação.txt", "r") as file:
                anotacoes = file.readlines()
            if not anotacoes:
                print("Nenhuma anotação encontrada.")
                return
            print("Anotações encontradas:")
            for i, linha in enumerate(anotacoes, 1):
                print(f"{i}. {linha.strip()}")

            indice = int(input("Digite o número da anotação que deseja excluir: "))
            if 1 <= indice <= len(anotacoes):
                removida = anotacoes.pop(indice - 1)
                with open("anotação.txt", "w") as file:
                    file.writelines(anotacoes)
                print(f"Anotação removida: {removida.strip()}")
            else:
                print("Número inválido. Nenhuma anotação removida.")

    except FileNotFoundError:
            print("Nenhuma anotação encontrada.")
    except ValueError:
            print("Por favor, digite um número válido.")

while True:
    print("🇳‌🇾‌🇩‌🇦‌🇮‌🇱‌🇾‌")
    print("1 - Criar anotações")
    print("2 - Ler anotações")
    print("3 - Excluir anotações")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    limpar_tela()

    if opcao == "1":
        criar_anotacao()

    elif opcao == "2":
        ler_anotacao()

    elif opcao == "3":
        excluir_anotacao()

    elif opcao == "4":
        print("Fechando!")
        break

    else:
        print("Opção inválida. Tente novamente.")
