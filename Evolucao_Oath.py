# Importações:
import random
from Probabilidades import quantpesoevo, quantvaloresevo, limite_maxatri, limite_minatri
 

# Função para gerar a evolução:
def evo_oath(oath):
    
    # Extraindo informações que são passadas como parametro:
    maxatribase = dict(oath['Max Atributos'])
    constier = oath['Tier']
    tier = constier
    
    # Atributos maximos para geração:
    maxatrievo1 = dict(maxatribase)
    maxatrievo2 = dict()
    # Dicionario com atributos vazios pra serem preenchidos:
    atrievo1 = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
    atrievo2 = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}

    # Definindo quantas evoluções terá:
    quantidadesortev = random.choices(quantvaloresevo[tier], weights=quantpesoevo[tier], k=1)[0]  # k=1 retorna uma lista com um único elemento.
    # Tranformando o valor de lista para inteiro:
    quantidadevo = int(quantidadesortev)

    # Criando uma lista para guardar as evoluções:
    evolucao = []
    
    # Caso o Oath tenha 2 evoluções, ele passa pelo primeiro if gerando a sua ficha de evolução
    # estagio 1, e caso só tenha uma evolução, ele ainda entra na checagem do primeiro if
    # já que ele será maior que 0 (neste caso 1).

    # Primeira evolução:
    if quantidadevo > 0:
        while True:
            # Aumenta o Tier do Oath em +1 antes de fazer a logica de evolução:
            tier += 1          
            # Caso por algum motivo o else não funcione e ele armazene dados antigos no tier e 
            # passe do valor maximo, este if concerta, para ser corrigido na proxima interação:
            if tier > 4:
                tier = constier
            # Inicia a Logica de aumento de atributos:
            total = 0 # Cria a variavel que irá guardar o total dos valores a serem testados no if abaixo.
            # Inicio da distribuição:
            for attr in maxatribase.keys():
                vlr = random.randint(-1, 2) # Adiciona de -1 a 2 em vlr.
                maxatrievo1[attr] += vlr # Soma o valor de vlr a um atributo.
                # Como no sistema não existe valor 2, o 3 é o menor, caso algum valor seja menor
                # do que 3 ele é automaticamente corrijido:
                if maxatrievo1[attr] < 3:
                    maxatrievo1[attr] = 3
                total += maxatrievo1[attr] # Guarda o valor em total.
            # Checando se o oath após a evolução, não fica fora dos parametros:
            if limite_minatri[tier] <= total <= limite_maxatri[tier]:
                break
            else:
                tier = constier
                maxatrievo1 = dict(maxatribase)

    # Segunda evolução:
    if quantidadevo == 2:
        # Passa os valores da primeira evolução para a segunda:
        maxatrievo2 = dict(maxatrievo1)
        # Inicia a lógica da segunda evolução:
        while True:
            # Aumenta o Tier do Oath em +1 antes de fazer a logica de evolução:
            tier += 1
            # Caso por algum motivo o else não funcione e ele armazene dados antigos no tier e 
            # passe do valor maximo, este if concerta, para ser corrigido na proxima interação:
            if tier > 4:
                tier = constier + 1 # O constier está +1 pois o padrão para evoluções em segundo estagio, é ser 1 a mais que a base, para ser aumentado na logica em 1 a mais do primeiro estagio.
            total = 0 # Cria a variavel que irá guardar o total dos valores a serem testados no if abaixo.
            # Inicio da distribuição:
            for attr in maxatrievo1.keys():
                vlr = random.randint(-1, 2) # Adiciona de -1 a 2 em vlr.
                maxatrievo2[attr] += vlr # Soma o valor de vlr a um atributo.
                # Como no sistema não existe valor 2, o 3 é o menor, caso algum valor seja menor
                # do que 3 ele é automaticamente corrijido:
                if maxatrievo2[attr] < 3:
                    maxatrievo2[attr] = 3
                total += maxatrievo2[attr] # Guarda o valor em total.
            # Checando se o oath após a evolução, não fica fora dos parametros:
            if limite_minatri[tier] <= total <= limite_maxatri[tier]:
                break
            else:
                tier = constier + 1
                maxatrievo2 = dict(maxatrievo1)

    # Distribuindo os atributos de cada evolução:
    # 1º evolução:
    if quantidadevo > 0:
        for attr in maxatrievo1:
            if maxatrievo1[attr] == 4:
                atrievo1[attr] = 2
            elif maxatrievo1[attr] == 7:
                atrievo1[attr] = 3
            elif maxatrievo1[attr] == 8:
                atrievo1[attr] = 4
            elif maxatrievo1[attr] == 9:
                atrievo1[attr] = 5
            else:
                atrievo1[attr] = max(maxatrievo1[attr] - 3, 1)
    # 2º evolução:
    if quantidadevo == 2:
        for attr in maxatrievo2:
            if maxatrievo2[attr] == 4:
                atrievo2[attr] = 2
            elif maxatrievo2[attr] == 7:
                atrievo2[attr] = 3
            elif maxatrievo2[attr] == 8:
                atrievo2[attr] = 4
            elif maxatrievo2[attr] == 9:
                atrievo2[attr] = 5
            else:
                atrievo2[attr] = max(maxatrievo2[attr] - 3, 1)
    
    # Soma dos Maximos atributos dos Oaths:
    totalevo1 = sum(maxatrievo1.values())
    totalevo2 = sum(maxatrievo2.values())
    
    # Agora após tudo já distribuido atualiza os pontos de vida dos Oaths:
    pvtotalevo1 = (oath['Pv Base'] + 1) + atrievo1['Durabilidade']
    pvtotalevo2 = (oath['Pv Base'] + 2) + atrievo2['Durabilidade']
    
    # Guardando as evoluções do Oath e seus atributos já distribuidos:
    evolucao.append({
        'MaxAtri 1º Evolução': maxatrievo1,
        'Atri 1º Evolução': atrievo1,
        'Pt. Total Evo 1': totalevo1,   
        'Pv Evo 1': pvtotalevo1,            
        'MaxAtri 2º Evolução': maxatrievo2,
        'Atri 2º Evolução': atrievo2,
        'Pt. Total Evo 2': totalevo2,   
        'Pv Evo 2': pvtotalevo2,          
        'Quant. Evoluções': quantidadevo  
    })
    
    return evolucao