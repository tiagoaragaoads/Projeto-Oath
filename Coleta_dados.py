# Importações Úteis:
import os
import time
# Importações de Integração:
from Regras_dados import Tiercomum, Tierslenda

def limpar():
    os.system('cls')

# Função especifica apenas para interação com usuário para coleta das informações:
def coleta_dados():
    # Aparência do Menu:
    limpar()
    print("=" * 50)
    print("🔮 Bem-vindo ao Gerador de Oaths! 🔮")
    print("=" * 50)
    print("\n")
    Tiercomum()
    
    while True:
        # Usuário irá escolher agora dentro da função se quer gerar aleatoriamente ou 
        # especificar o tier:
        print("=" * 50)
        print("1. 🔮 Gerar Oath's Aleatoriamente! 🔮")
        print("2. 🔮 Gerar Oath's com Tier Específico! 🔮")
        print("=" * 50)

        try:
            escolha = int(input(">>> "))

            # Fazendo tratamento para caso a escolha do usuário seja incorreta:
            if escolha < 1 or escolha > 2:
                print("Opção inválida! Digite uma opção válida!")
                input("Pressione ENTER para voltar para o menu ...")
                limpar()
                continue  

            # Opção de geração aleatória:
            if escolha == 1:
                escolha = 'Random'
                while True:
                    try:
                        limite = int(input("✨ Quantos Oath's você gostaria de gerar? (Digite um número) --> "))
                        # Caso escolha aleatorio, o tier recebe None, onde no programa de 
                        # geração eu identifico e entrego a ele valores aleatorios:
                        tier = None 
                        break
                    except ValueError:
                        print("Valor inválido! Digite uma opção válida!")

            # Opção de geração específica:
            elif escolha == 2:
                while True:
                    try:
                        tier = int(input("\nQual o tier do Oath que você quer gerar? Ex.: 1 seria Branco --> "))
                        limite = int(input("✨ Quantos Oath's você gostaria de gerar? (Digite um número) --> "))
                        break
                    except ValueError:
                        print("Valor inválido! Digite uma opção válida!")

            break

        except ValueError:
            print("Digitação inválida! Por favor, digite corretamente!")
            time.sleep(1)
            limpar()
    
    return tier, limite, escolha # Retorno os valores que serão usados.

# Segue o mesmo principio da coleta_dados:
def coleta_dados_lendario():
    # Aparência do Menu:
    limpar()
    print("=" * 50)
    print("🔮 Bem-vindo ao Gerador de Oaths Lendarios! 🔮")
    print("=" * 50)
    print("\n")
    Tierslenda()  # Verifique se a função Tierslenda() está definida corretamente
    
    while True:
        # Usuário irá escolher agora dentro da função se quer gerar aleatoriamente ou especificar o tier.
        print("=" * 50)
        print("1. 🔮 Gerar Oath's Aleatoriamente! 🔮")
        print("2. 🔮 Gerar Oath's com Tier Específico! 🔮")
        print("=" * 50)

        try:
            escolha = int(input(">>> "))

            # Tratamento para caso a escolha do usuário seja incorreta:
            if escolha < 1 or escolha > 2:
                print("Opção inválida! Digite uma opção válida!")
                input("Pressione ENTER para voltar para o menu ...")
                limpar()
                continue  

            # Opção de geração aleatória:
            if escolha == 1:
                escolha = 'Random'
                while True:
                    try:
                        limite = int(input("✨ Quantos Oath's você gostaria de gerar? (Digite um número) --> "))
                        tier = None
                        break
                    except ValueError:
                        print("Valor inválido! Digite uma opção válida.")

            # Opção de geração específica:
            elif escolha == 2:
                escolha = None
                while True:
                    try:
                        tier = int(input("\nQual o tier do Oath que você quer gerar? Ex.: 6 seria Laranja --> "))
                        # Verifique se o tier está dentro do intervalo aceitável:
                        if tier < 6 or tier > 8: 
                            print("Tier inválido! Digite um número entre 6 e 8.")
                            continue
                        limite = int(input("✨ Quantos Oath's você gostaria de gerar? (Digite um número) --> "))
                        break
                    except ValueError:
                        print("Valor inválido! Digite uma opção válida.")
            break

        except ValueError:
            print("Digitação inválida! Por favor, digite corretamente!")
            time.sleep(1)
            limpar()
    
    limpar()
    return tier, limite, escolha
