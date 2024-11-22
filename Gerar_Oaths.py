# Importações de bibliotecas:
import random

# Importações gerais:
from Gerar_Nomes import Gerar_Nomes_Random
from Probabilidades import valores, peso, valoreslend, pesolend, limite_maxatri, limite_minatri
from Dados_importantes import vantagens, estilos, tipos

def gerar_oath(tier, limite, escolha):
    # Lista para armazenar os Oaths gerados:
    Oaths_Gerados = []
    
    # Converte as chaves dos dicionários em LISTA para sorteio com random.choice:
    est = list(estilos.keys())
    vant = list(vantagens.keys())
    
    if tier is None:
        tier = 0
    
    for comeco in range(limite):
        
        # Definindo o tier aleatoriamente, se não fornecido
        if escolha == 'Random':
            tier = random.randint(1, 5)            
        
        # Declara e reinicia os atributos para cada Oath:
        maxatri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        atri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        
        # Sorteia uma vantagem, uma natureza e um tipo para o Oath:
        estsort = random.choice(est)
        vantsort = random.choice(vant)
        tiposort = random.choice(tipos)
        
        # Sorteia se é ou não é Shiny
        if random.random() < 0.05:
            shiny = 1     
        else:
            shiny = 0
        
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
                dado = random.choices(valores[tier], peso[tier])[0]
                maxatri[attr] = dado
                soma += maxatri[attr]
            # Tratamento para que os Oaths não ultrapassem os limites
            if limite_minatri[tier] <= soma <= limite_maxatri[tier]:
                break
        
        # Definindo so atributos base de cada Oath:
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
                atri[attr] = max(maxatri[attr] -3, 1)

        # Define os Pv's baseados no Tier:
        if tier == 1:
            Pv = random.randint(2, 3)
        elif tier in [2, 3]:
            Pv = random.randint(3, 4)
        elif tier == 4:
            Pv = random.randint(4, 5)
        else:
            Pv = random.randint(5, 6)

        # Define os pontos de vida já calculados:
        pvtotal = Pv + atri['Durabilidade']
        
        # Aumentando o HP caso o Oath seja Shinny:
        if shiny == 1:
            pvtotal += 1
        
        # Pegando o nome e o sexo do Oath:
        nome, sexo = Gerar_Nomes_Random()

        # Guardando cada Oath:
        Oaths_Gerados.append({
            'Nome': nome,
            'Sexo': sexo,
            'Tier': tier,
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

def gerar_oath_lendario(tier, limite, escolha):
    # Lista para armazenar os Oaths gerados:
    Oaths_Lendarios = []
    
    # Converte as chaves dos dicionários em LISTA para sorteio com random.choice:
    est = list(estilos.keys())
    vant = list(vantagens.keys())
    
    # Inicio do programa:
    for comeco in range(limite):
        # Definindo o tier aleatoriamente, se não fornecido
        if escolha == 'Random':
            tier = random.randint(6,8)
            
        # Declara e reinicia os atributos para cada Oath:
        atri_lendario = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
        
        # Sorteia uma vantagem, uma natureza e um tipo para o Oath:
        estsort = random.choice(est)
        vantsort = random.choice(vant)
        tiposort = random.choice(tipos)
        
        # Sorteia se é ou não é Shiny
        if random.random() < 0.05:
            shiny = 1     
        else:
            shiny = 0
        
        # Sorteia tipos adicionais com 40% de chance:
        if random.random() < 0.4:
            restypes = [tipo for tipo in tipos if tipo != tiposort]
            # Corrigindo para que ele não escolha um tipo que o Oath já tenha:
            sectipos = random.choice(restypes) if restypes else None 
        # Caso o sorteio nao der os 40% ele aderir valor Nulo a sectipos:
        else:
            sectipos = None
            
        # Definindo os atributos de forma aleatoria do Tier do Oath escolhido:
        for lendatri in atri_lendario.keys():
            dado = random.choices(valoreslend[tier], pesolend[tier])[0]
            atri_lendario[lendatri] = dado

        # Define os Pv's baseados no Tier:
        if tier == 6:
            Pv = random.randint(6,7)
        elif tier == 7:
            Pv = random.randint(6,8)
        else:
            Pv = random.randint(7,9)
            
        # Define os pontos de vida totais do Oath Lendário:
        Pvtotal = Pv + atri_lendario["Durabilidade"]
        # Define os pontos de mana totais do Oath Lendário:
        Manatotal = atri_lendario["Foco"]
        # Caso o Oath seja shinny ocorre o aumento de atributo:
        if shiny == 1:
            Pvtotal += 1
            Manatotal += 1
        
        nome, sexo = Gerar_Nomes_Random()

        # Guardando cada Oath:
        Oaths_Lendarios.append({
            'Nome': nome,
            'Sexo': sexo,
            'Tier': tier,
            'Max Atributos': atri_lendario,
            'Pv': Pvtotal,
            'Mana': Manatotal,
            'Shiny': shiny,
            'Vantagem': vantsort,
            'Estilo': estsort,
            'Tipo': tiposort,
            'Tipo Secundário': sectipos
        })
        
    if tier is None:  
        tier = None  # Permite gerar um novo tier na próxima iteração
    else:
        tier = None  # Para não modificar o tier em gerações futuras
        
    return Oaths_Lendarios