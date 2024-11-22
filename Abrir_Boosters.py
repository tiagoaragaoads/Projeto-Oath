# Abrir boosters:
# O obejtivo é criar boosters para enviar o gerador de oaths criaturas especificas.
# Provavelmente as duas funçoes. Gerar lendarios e gerar comuns serão chamadas aqui:

# Primeiramente eu quero fazer pelo menos 3 boosters padrões para testes:
# 1º Starter booster: Deve conter garantido uma criatura de tier 2, e outras duas criaturas
# aleatorias entre Tier I, II e III

# Importações de biblioteca:
import os
import random
# Importações de dados:
from Probabilidades_Boosters import startertier, starterpeso

def starter_booster():
    # Variavel lista que irá receber os tiers:
    # Como o starter pack ja tem um tier 2 garantido, ele já vem com esse valor na lista:
    tier = [2]
    # Aqui a variavel limite que ira indicar que é necessario gerar 3 oaths.
    limite = 3
    # Aqui fica a variavel escolha que irá indicar ao programa de geração que o modelo de criação
    # é de booster, dessa forma podendo anexar um tratamento personalizado de geração:
    escolha = 'Booster'
    
    # Variavel que repeti o sorteio uma quantidade de vezes que é definida pelo booster
    # neste caso 2 já que o terceiro já está pre-definido:
    for i in range(2):
        sortier = int(random.choices(startertier, weights=starterpeso,k=1)[0]) # Sorteando e guardando.
        tier.append(sortier) # adicionando valor a lista tier.
    
    print(f"Valor Sorteado: {tier}")
    return tier, limite, escolha
