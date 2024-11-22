# testar para evoluções aceitarem valores em lista:
# Importações:
import random
from Probabilidades import quantpesoevo, quantvaloresevo, limite_maxatri, limite_minatri
from Probabilidades import valores, peso, valoreslend, pesolend, limite_maxatri, limite_minatri
from Dados_importantes import vantagens, estilos, tipos
from Gerar_Nomes import Gerar_Nomes_Random


def gerar_oath(tier, limite, escolha):
    # Lista para armazenar os Oaths gerados:
    Oaths_Gerados = []
    
    # Converte as chaves dos dicionários em LISTA para sorteio com random.choice:
    est = list(estilos.keys())
    vant = list(vantagens.keys())
    
    # Caso o tier seja uma lista, transformamos ela em um iterador
    if isinstance(tier, list):
        tier_iter = iter(tier)
    else:
        tier_iter = [tier]  # Se for único, coloca em uma lista
    
    for comeco in range (limite):
        # Define o tier a ser usado, pegando do iterador ou gerando aleatório
        if escolha == 'Random':
            current_tier = random.randint(1, 5)            
        else:
            try:
                current_tier = next(tier_iter)  # Pega o próximo tier da lista
            except StopIteration:
                break  # Para de gerar se não houver mais tiers na lista
        
        # Declara e reinicia os atributos para cada Oath:
        maxatri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        atri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        
        # Sorteia uma vantagem, uma natureza e um tipo para o Oath:
        estsort = random.choice(est)
        vantsort = random.choice(vant)
        tiposort = random.choice(tipos)
        
        # Sorteia se é ou não é Shiny
        shiny = 1 if random.random() < 0.05 else 0
        
        # Sorteia tipos adicionais com 40% de chance:
        if random.random() < 0.4:
            restypes = [tipo for tipo in tipos if tipo != tiposort]
            sectipos = random.choice(restypes) if restypes else None 
        else:
            sectipos = None
            
        # Definindo os atributos máximos de forma aleatória do Tier do Oath escolhido:
        while True:
            soma = 0
            for attr in maxatri.keys():
                dado = random.choices(valores[current_tier], peso[current_tier])[0]
                maxatri[attr] = dado
                soma += maxatri[attr]
            # Tratamento para que os Oaths não ultrapassem os limites
            if limite_minatri[current_tier] <= soma <= limite_maxatri[current_tier]:
                break
        
        # Definindo os atributos base de cada Oath:
        for attr in maxatri:
            if maxatri[attr] == 4:
                atri[attr] = 2
            elif maxatri[attr] == 7:
                atri[attr] = 4
            elif maxatri[attr] == 8:
                atri[attr] = 4
            elif maxatri[attr] == 9:
                atri[attr] = 5
            else:
                atri[attr] = max(maxatri[attr] - 3, 1)

        # Define os Pv's baseados no Tier:
        if current_tier == 1:
            Pv = random.randint(2, 3)
        elif current_tier in [2, 3]:
            Pv = random.randint(3, 4)
        elif current_tier == 4:
            Pv = random.randint(4, 5)
        else:
            Pv = random.randint(5, 6)

        # Define os pontos de vida já calculados:
        pvtotal = Pv + atri['Durabilidade']
        
        # Aumentando o HP caso o Oath seja Shiny:
        if shiny == 1:
            pvtotal += 1
        
        # Pegando o nome e o sexo do Oath:
        nome, sexo = Gerar_Nomes_Random()

        # Guardando cada Oath:
        Oaths_Gerados.append({
            'Nome': nome,
            'Sexo': sexo,
            'Tier': current_tier,
            'Max Atributos': maxatri,
            'Atributos': atri,
            'Pv Total': pvtotal,
            'Pv Base': Pv,
            'Shiny': shiny,
            'Vantagem': vantsort,
            'Estilo': estsort,
            'Tipo': tiposort,
            'Tipo Secundário': sectipos,
            'Total': soma
        }) 
    
    return Oaths_Gerados

# Função para gerar a evolução:

def evo_oath(oath):
    
    # Extraindo informações que são passadas como parâmetro:
    maxatribase = dict(oath['Max Atributos'])
    constiers = oath['Tier']  # Agora 'Tier' é uma lista de tiers
    evolucao = []  # Lista para guardar as evoluções
    
    print(type(constiers)) # Print teste
    
    # Iterando sobre cada tier na lista de tiers:
    for tier in constiers:
        
        # Atributos máximos para geração:
        maxatrievo1 = dict(maxatribase)
        maxatrievo2 = dict()
        
        # Dicionário com atributos vazios para serem preenchidos:
        atrievo1 = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        atrievo2 = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}

        # Definindo quantas evoluções terá:
        quantidadesortev = random.choices(quantvaloresevo[tier], weights=quantpesoevo[tier], k=1)[0]  
        quantidadevo = int(quantidadesortev)

        # Primeira evolução:
        if quantidadevo > 0:
            while True:
                # Aumenta o Tier do Oath em +1 antes de fazer a lógica de evolução:
                tier += 1          
                if tier > 4:
                    tier = constiers[0]  # Reseta para o valor inicial do primeiro tier
                total = 0
                # Início da distribuição:
                for attr in maxatribase.keys():
                    vlr = random.randint(-1, 2)
                    maxatrievo1[attr] += vlr
                    if maxatrievo1[attr] < 3:
                        maxatrievo1[attr] = 3
                    total += maxatrievo1[attr]
                if limite_minatri[tier] <= total <= limite_maxatri[tier]:
                    break
                else:
                    tier = constiers[0]  # Reseta novamente se estiver fora do limite
                    maxatrievo1 = dict(maxatribase)

        # Segunda evolução:
        if quantidadevo == 2:
            maxatrievo2 = dict(maxatrievo1)
            while True:
                tier += 1
                if tier > 4:
                    tier = constiers[0] + 1  # O constier está +1 pois o padrão para evoluções de segundo estágio é 1 a mais que o primeiro
                total = 0
                for attr in maxatrievo1.keys():
                    vlr = random.randint(-1, 2)
                    maxatrievo2[attr] += vlr
                    if maxatrievo2[attr] < 3:
                        maxatrievo2[attr] = 3
                    total += maxatrievo2[attr]
                if limite_minatri[tier] <= total <= limite_maxatri[tier]:
                    break
                else:
                    tier = constiers[0] + 1
                    maxatrievo2 = dict(maxatrievo1)

        # Distribuindo os atributos de cada evolução:
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

        pvtotalevo1 = (oath['Pv Base'] + 1) + atrievo1['Durabilidade']
        pvtotalevo2 = (oath['Pv Base'] + 2) + atrievo2['Durabilidade']

        # Guardando as evoluções do Oath e seus atributos distribuídos:
        evolucao.append({
            'MaxAtri 1º Evolução': maxatrievo1, 
            'Atri 1º Evolução': atrievo1,       
            'Pv Evo 1': pvtotalevo1,            
            'MaxAtri 2º Evolução': maxatrievo2, 
            'Atri 2º Evolução': atrievo2,       
            'Pv Evo 2': pvtotalevo2,            
            'Quant. Evoluções': quantidadevo    
        })
    return evolucao


tier = [1,2,3,4,5]
limite = 5
Escolha = None

oath_gerado = gerar_oath(tier, limite, Escolha)
evoluc = evo_oath(oath_gerado)
