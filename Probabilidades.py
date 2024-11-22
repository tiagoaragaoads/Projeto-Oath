# Chances para sortear o tempo que este oath demora para evoluir em Evolucao_Oath:
chance_evo = [1,2,3,4]
peso_c_evo = [0.10, 0.10, 0.10, 0.10]

# Define quais atributos e suas probabilidades por TIER:
peso = {
    1: [0.30, 0.60, 0.10],
    2: [0.15, 0.45, 0.35, 0.05],
    3: [0.05, 0.35, 0.35, 0.15, 0.10],
    4: [0.25, 0.30, 0.20, 0.15, 0.10],
    5: [0.15, 0.25, 0.25, 0.15, 0.10, 0.05]
}
valores = {
    1: [3,4,5],
    2: [3,4,5,6],
    3: [3,4,5,6,7],
    4: [4,5,6,7,8],
    5: [4,5,6,7,8,9],
}

# Define quais atributos e suas probabilidades por TIER, mas para Lendários:
pesolend = {
    6: [0.1, 0.2, 0.3, 0.3, 0.1],
    7: [0.1, 0.2, 0.35, 0.25, 0.1],
    8: [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]
}
valoreslend = {
    6: [3,4,5,6,7],
    7: [4,5,6,7,8],
    8: [4,5,6,7,8,9],
}

# Define probabilidades de ter moves de power de 1 a 6:
pesomoves = [
    0.15,
    0.2,
    0.2,
    0.15,
    0.1,
    0.1
]
valoresmoves = [
    1,
    2,
    3,
    4,
    5,
    6
]

# Define probabilidade de ter ou não uma evolução:
# Quantas evoluções vai ter:
quantpesoevo = {
    1: [0.30, 0.40, 0.30], # Tier 1: 80% de ter 1 Evolução, 20% de ter 2.
    2: [0.25,0.70,0.05], # Tier 2: 15% de não ter nenhuma Evolução, 70% de ter 1 e 15% de ter 2.
    3: [0.70,0.25,0.05], # Tier 3: 70% de não ter nenhuma Evolução, 25% de ter 1 e 5% de ter 2.
    4: [0.95,0.05], # Tier 4: 95% de não ter Evolução, 5% de ter 1.
    5: [1] # Tier 5: Não tem Evolução.
}
quantvaloresevo = {
    1: [0,1,2], # Tier 1: Branco
    2: [0,1,2], # Tier 2: Verde
    3: [0,1,2], # Tier 3: Azul
    4: [0,1], # Tier 4: Roxo
    5: [0] # Tier 5: Preto Não tem evolução.
}

# Ainda não estou usando!
# Valores que serão adicionados:
valoresevo = [0,1,2]
# Peso dos valores acima:
pesoevo = [0.30,0.60,0.10] # O valor: 0, só é para pular para proxima casa, sem disbruir fazendo o ciclo ser mais demorado, e em teoria, distribuindo melhor os atributos.
# FIM

# Define o limite máximo para o maxatri, tornando os Oath's em teoria mais balanceados:
limite_minatri = {
    1: 15,
    2: 15,
    3: 20,
    4: 20,
    5: 25,
}
limite_maxatri = {
    1: 18,
    2: 20,
    3: 25,
    4: 28,
    5: 32,
}