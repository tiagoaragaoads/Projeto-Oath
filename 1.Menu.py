# Aqui é a área principal do código, onde terá apenas as importações para chamar cada
# função necessária.

# Importações de biblioteca:
import os

# Importando as funções:
from Exibir_Oaths import exibir_lendario, exibir_comum
from Coleta_dados import coleta_dados, coleta_dados_lendario
from Gerar_Oaths import gerar_oath, gerar_oath_lendario
from Evolucao_Oath import evo_oath
from Abrir_Boosters import starter_booster
from Regras_dados import Tierslenda, Tiercomum
from Dados_importantes import exibir_ficha_jogador, ficha_jogadorAT, ficha_jogadorMX
from Gerar_Nomes import Gerar_Nomes_Random

# Limpando a tela:
def limpar():
    os.system('cls')

# Chamando as variáveis:
esc = 0

while True: # Loop Infinito:
    
    # Exibição do Menu:
    print("===================================")
    print("        🌟 Menu Principal 🌟      ")
    print("===================================")
    print("1. ✨ Gerar Oath's ✨")
    print("2. 🎴 Abrir Boosters 🎴")
    print("3. 📜 Regras 📜")
    print("4. ❌ Sair ❌ ")
    print("===================================")

    # Interação para decisão do usuário:
    esc = int(input("Escolha a opção desejada: "))
    # Limpar tela após escolha:
    limpar()
    
    # Escolha 1: Gerar Oath's;
    if esc == 1:
        # Exibição de menu:
        print("===================================")
        print("       🌟 Menu de Geração 🌟      ")
        print("===================================")
        print("1. ✨ Gerar Oath's Comuns ✨")
        print("2. 🌟 Gerar Oath's Lendários 🌟")
        print("===================================")
        
        # Interação para decisão do usuário:
        esc = int(input("Escolha a opção desejada: "))
        limpar()
        
        # Escolha 1: Gerando Comuns:
        if esc == 1:
            # Executando a função de coleta de dados e descompactando:
            tier, limite, escolha = coleta_dados()
            # Passando os dados para gerar_oath:
            oath_comum = gerar_oath(tier, limite, escolha)
            # Passando os dados dos Oath's gerados para evolução:
            # como a função evo_oath espera apenas um dicionario(oath) de cada vez, eu descompacto
            # utilizando um for para ela enviar apenas um oath e exibir um oath por vez.
            for oath in oath_comum:
                evolucao = evo_oath(oath)
                # Finalizando agora com a exibição dos oaths gerados e suas evoluções:
                exibir_comum(oath, evolucao)
            # Voltar ao menu e limpar tela:
            input("Precione ENTER para voltar ao menu ...")
            limpar()
        
        # Escolha 2: Gerar Lendário.
        elif esc == 2:
            # Executando a função de coleta de dados e descompactando:
            tier, limite, escolha = coleta_dados_lendario()
            # Passando os dados para gerar o oath lendario:
            oaths_lendarios = gerar_oath_lendario(tier, limite, escolha)
            # Agora finalizando realizando a exibição:
            for oath in oaths_lendarios:
                exibir_lendario(oath)
                print("\n")
            # Pausa o programa para dar tempo do usuário ver os Oath's Gerados:
            input("Precione ENTER para voltar ao menu ...")
            limpar()
        else:
            print("escolha incorreta, teste novamente")
        
    
    # Escolha 2: Abrir Boosters; AINDA NÃO ESTÁ IMPLEMENTADO;
    elif esc == 2:
        # Executando a função de coleta de dados e descompactando:
        tier, limite, escolha = starter_booster()
        # Passando os dados para gerar_oath:
        oath_comum = gerar_oath(tier, limite, escolha)
        # Passando os dados dos Oath's gerados para evolução:
        # como a função evo_oath espera apenas um dicionario(oath) de cada vez, eu descompacto
        # utilizando um for para ela enviar apenas um oath e exibir um oath por vez.
        for oath in oath_comum:
            evolucao = evo_oath(oath)
            # Finalizando agora com a exibição dos oaths gerados e suas evoluções:
            exibir_comum(oath, evolucao)
        # Voltar ao menu:
        input("Precione ENTER para voltar ao menu ...")
        limpar()
    
    # Escolha 5: Teste de Geração de nomes: NÃO CONSTA NO MENU;
    elif esc == 5:
        # Quantidade de nomes que será gerado:
        esc = int(input("Quantos nomes você deseja gerar? >>> "))
        cont = 0
        # Gera a quantidade de nomes:
        for i in range(esc):
            # Funçao que esta em Gerar_Nomes:
            nome, sexo = Gerar_Nomes_Random() # Função que gera os nomes.
            # Variavel que guarda quantos nomes foram gerados:
            cont += 1
            # Exibe os nomes:
            print(f"{cont}: {nome} ({sexo})")
        # Voltar ao menu:
        input("Precione ENTER para voltar ao menu ...")
        limpar()