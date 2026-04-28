#### - Criar uma estrutura de dados com os componentes
# de um quadro elétrico à vossa escolha.
# Menciona as especificações dos componentes

quadro_eletrico = {
    "corte_geral" : {
        "In" : 32,
    },
    "diferencial" : {
        "deltaI" : 0.03,
        "In" : 32
    },
    "dijuntor1": {
        "In" : 10
    },
    "dijuntor2": {
        "In" : 16
    }
}

lampadas = {
    "potencia" : 40,
    "tensao" : 230,
    "quantidade" : 3
}

def calcular_corrente(potencia, tensao):
    corrente = potencia / tensao
    return corrente

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)
corrente_de_cada_lampada = calcular_corrente(lampadas["potencia"], lampadas["tensao"])
print(corrente_de_cada_lampada)

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)

corrente_de_todas_as_lampadas = corrente_de_cada_lampada * lampadas["quantidade"]
corrente_de_todas_as_lampadas

def selecionar_disjuntor(valor):
    if valor < 6:
        print("C6")
    elif valor >= 6 and valor < 10:
        print("C10")
    elif valor >= 10 and valor < 16:
        print("C16")
    elif valor >= 16 and valor < 20:
        print("C20")
    elif valor >= 20 and valor < 25:
        print("C25")

selecionar_disjuntor(corrente_de_todas_as_lampadas)