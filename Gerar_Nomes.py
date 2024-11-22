# Gera Nomes Aleatórios baseados em Prefixo, Sufixo e Silabas:

# Importações:
import random
#from Gerar_Oath import sexo

def sexo_oath():
    genero = ['♂ Masculino', '♀ Feminino']
    sexo = random.choice(genero)
    return sexo

def Gerar_Nomes_Random():
    
    # Pegando o sexo do Oath da função sexo_oath:
    sexo = sexo_oath()
    # Gerando um nome vazio para ser preenchido:
    nome = ""  
    
    # Listas de prefixos, sufixos, titulos e sílabas:
    
    # Para nomes masculinos:
    titulos_masc = [
    "Dr.", "Sr.", "Eng.", "Prof.", "Adv.", "Arq.", "M.", "Ps.", 
    "T.", "Capt.", "Gen.", "P.", "Mec.", "Enf.", "C."
    ]
    prefixos_masc = [
    "Ael", "Al", "Ari", "Astra", "Bai", "Bar", "Bari", "Bel", "Boko",
    "Cai", "Cal", "Cer", "Chai", "Dai", "Dar", "Drax", "Dur", "Elys",
    "Ember", "Erae", "Fai", "Fen", "Gai", "Garae", "Gal", "Gry", 
    "Hal", "Hala", "Hari", "Hel", "Hyn", "Isar", "Jai", "Jan", 
    "Jas", "Jora", "Ka", "Kael", "Kall", "Kai", "Kano", "Kari", 
    "Kiro", "Kyra", "La", "Lano", "Mai", "Mar", "Myn", "Nai", 
    "Neko", "Nyl", "Odin", "Oris", "Ora", "Orin", "Pari", "Piko", 
    "Ra", "Rael", "Riven", "Sai", "Sari", "Sel", "Sera", "Talon", 
    "Val", "Vex", "Vira", "Wai", "Wren", "Xen", "Yly", "Zai", 
    "Zor", "Zyn", "Ku"
    ]
    silabas_masc = [
    "ba", "be", "bi", "bu", "ca", "cha", "da", "de", "di", "do", 
    "du", "ga", "ge", "gi", "ha", "he", "hi", "ho", "ja", "je", 
    "ji", "ka", "ke", "ki", "ku", "ma", "me", "mi", "mo", "na", 
    "ne", "ni", "no", "pa", "pe", "pi", "ra", "ri", "ro", "sa", 
    "ta", "te", "ti", "va", "ve", "vi", "za", "zai", "ze", "zi"
    ]
    sufixos_masc = [
    "ach", "air", "al", "an", "ar", "as", "dão", "dan", "dor", 
    "du", "el", "en", "ex", "gão", "ia", "ian", "ich", "ik", 
    "in", "inor", "ion", "ir", "ith", "ithor", "ithra", "ka", 
    "kan", "lin", "lyon", "ol", "on", "or", "osis", "oth", 
    "rel", "ris", "rion", "ran", "s", "th", "thinho", "ul", 
    "un", "ur", "wyn", "yth", "yra", "yn"
    ]
    
    # Para nomes femininos:
    titulos_fem = [
    "Dra.", "Sra.", "Enga.", "Profa.", "Adva.", "Arqa.", "M.", 
    "Psa.", "T.", "Capa.", "Gen.", "Enfa.", "Mec.", "D.", "C."
    ]
    prefixos_fem = [
    "Alti", "Ara", "Ayla", "Brin", "Caro", "Calae", "Darae", 
    "Farae", "Gali", "Gos" ,"Iarae", "Jarae", "Larae", "Marae",
    "Nera", "Oris", "Quin", "Sarae", "Sora", "Tari", "Uma", "Zeni"
    ]
    silabas_fem = [
    "ai", "al", "an", "ar", "as", "at", "au", "e", "ei", "el", 
    "em", "en", "es", "et", "fa", "fai", "fo", "ha", "hai", "hu", 
    "lai", "li", "lo", "lu", "mai", "nai", "o", "pai", "po", 
    "rei", "ru", "sei", "shi", "si", "tai","to", "tu", "wu", "ya", 
    "ye", "yi", "xu", "xi", "wo", "yu", "yo", "zu"
    ]
    sufixos_fem = [
    "ael", "aen", "alith", "anith", "eth", "ethar", "iax", "iah", 
    "ilith", "inys", "ionel", "ionis", "ithra", "myr", "s", "sa", 
    "tal", "unel", "ver", "ythe", "ynar"
    ]

    # Gerando um nome masculino:
    if sexo == '♂ Masculino':
    # Chance de 5% de ter um titulo:
        if random.random() < 0.05:
            nome += random.choice(titulos_masc) + " "
    # Prefixo:
        nome += random.choice(prefixos_masc)
    # Chance de 15% de ter uma silaba:
        if random.random() < 0.15:
            nome += random.choice(silabas_masc)
    # Chance de 70% de ter um sufixo:
        if random.random() < 0.70:
            nome += random.choice(sufixos_masc)
    
    # Gerando um nome feminino:
    else:
        # Chance de 5% de ter um titulo:
        if random.random() < 0.05:
            nome += random.choice(titulos_fem) + " "
    # Prefixo:
        nome += random.choice(prefixos_fem)
    # Chance de 15% de ter uma silaba:
        if random.random() < 0.15:
            nome += random.choice(silabas_fem)
    # Chance de 70% de ter um sufixo:
        if random.random() < 0.70:
            nome += random.choice(sufixos_fem)
    
    # Retornando o nome já gerado:
    return nome, sexo