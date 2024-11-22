# Importando os dados de outras páginas:
from Dados_importantes import vantagens, estilos

def exibir_atri_comum(titulo, max_atributos, atributos):
    print(f"{titulo} 🌟")
    for attr in max_atributos:
        distribuido = '•' * atributos[attr]  # Bolinhas preenchidas
        distribuir = 'o' * (max_atributos[attr] - atributos[attr])  # Bolinhas não preenchidas
        print(f"🔹 {attr}: {distribuido}{distribuir}")
    print("=" * 50)
    
def exibir_atri_lendario(titulo, max_atributos):
    print(f"{titulo} 🌟")
    for attr in max_atributos:
        distribuido = '•' * max_atributos[attr]  # Bolinhas preenchidas
        print(f"🔹 {attr}: {distribuido}")
    print("=" * 50)

# Exibindo os Oaths comuns:
def exibir_comum(oath, evolucao):

    # 
    print("=" * 50)
    print("🔮 Oath Comum 🔮")
    print("=" * 50)
    print(f"🌟 Nome: {oath['Nome']}")
    print(f"⚧  Sexo: {oath['Sexo']}")
    print(f"🎯 Tier: {oath['Tier']}")
    print(f"🎯 Total de pontos: {oath['Total']}")
    print(f"🎯 Quantidade de evoluções: {evolucao[0]['Quant. Evoluções']}")

    if oath['Shiny'] == 1:
        print("🌟✨🌟✨ Seu Oath é um Shiny 🌟✨🌟✨")
        print("=" * 50)

    # Exibindo Atributos
    exibir_atri_comum("🌟 Atributo dos Oath's", oath['Max Atributos'], oath['Atributos'])

    # Exibição dos Pontos de Vida
    if oath['Shiny'] == 1:
        print(f"❤️ Pontos de Vida ❤️: {oath['Pv Total']} = {oath['Pv Base']} + {oath['Atributos']['Durabilidade']} + 1")
    else:
        print(f"❤️ Pontos de Vida ❤️: {oath['Pv Total']} = {oath['Pv Base']} + {oath['Atributos']['Durabilidade']}")
    
    print(f"Def. Fisica 🛡️🛡️: {oath['Atributos']['Durabilidade']}")
    print(f"Def. Mágica ✨🛡️: {oath['Atributos']['Foco']}")

    # Exibindo Vantagem
    vant = oath['Vantagem']
    des_vant = vantagens[vant]
    print("=" * 50)
    print(f"🌟 Vantagem: {vant}")
    print(f"Descrição: {des_vant}")

    # Exibindo Tipos
    print("🔥💧🌿Tipo🌿💧🔥")
    print(f"Tipo Principal: {oath['Tipo']}")
    if oath['Tipo Secundário'] is not None:
        print(f"Tipo Secundário: {oath['Tipo Secundário']}")

    # Exibindo Estilo de Combate
    est = oath['Estilo']
    desc_est = estilos[est]
    print("=" * 50)
    print("⚔️ Estilo de Combate ⚔️")
    print(f"{est}: {desc_est}")
    

    # Exibindo Evoluções se houver
    if oath['Tier'] < 5 and evolucao[0]['Quant. Evoluções'] > 0:
        print("=" * 50)
        print("🌟 - - - Evoluções - - - 🌟")
        print("=" * 50)
        print(f"Total de pontos: {evolucao[0]['Pt. Total Evo 1']}")
        exibir_atri_comum("🌟 1º Evolução", evolucao[0]['MaxAtri 1º Evolução'], evolucao[0]['Atri 1º Evolução'])
        print(f"❤️ Pontos de Vida ❤️: {evolucao[0]['Pv Evo 1']}")
        print("=" * 50)
        print(f"Total de pontos: {evolucao[0]['Pt. Total Evo 2']}")
        exibir_atri_comum("🌟 2º Evolução", evolucao[0]['MaxAtri 2º Evolução'], evolucao[0]['Atri 2º Evolução'])
        if evolucao[0]['Quant. Evoluções'] == 2:
            print(f"❤️ Pontos de Vida ❤️: {evolucao[0]['Pv Evo 2']}")
    print("\n")

# Exibindo os Oaths lendários:
def exibir_lendario(lendario):
    print("=" * 50)
    print("🔮 Oath Lendario 🔮")
    print("=" * 50)
    print(f"🌟 Nome: {lendario['Nome']}")
    print(f"⚧  Sexo: {lendario['Sexo']}")
    print(f"🎯 Tier: {lendario['Tier']}")

    # Exibindo Atributos
    exibir_atri_lendario("🌟 Atributos", lendario['Max Atributos'])

    if lendario['Shiny'] == 1:
        print("=" * 50)
        print("🌟✨ Seu Oath é um Shiny ✨🌟")
    print("=" * 50)
    print(f"❤️ Pontos de Vida ❤️: {lendario['Pv']}")
    print(f"✨ Pontos de Mana ✨: {lendario['Mana']}")
    print("=" * 50)

    # Exibindo Vantagem
    vant = lendario['Vantagem']
    des_vant = vantagens[vant]
    print("=" * 50)
    print(f"🌟 Vantagem: {vant}")
    print(f"🌟 Descrição: {des_vant}")

    # Exibindo Tipos
    print("🔥💧🌿Tipo🌿💧🔥")
    print(f"Tipo Principal: {lendario['Tipo']}")
    if lendario['Tipo Secundário'] is not None:
        print(f"Tipo Secundário: {lendario['Tipo Secundário']}")

    # Exibindo Estilo de Combate
    est = lendario['Estilo']
    desc_est = estilos[est]
    print("=" * 50)
    print("⚔️ Estilo de Combate ⚔️")
    print(f"{est}: {desc_est}")
    print("\n")