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

import minhas_funcoes

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)
corrente_de_cada_lampada = minhas_funcoes.calcular_corrente(lampadas["potencia"], lampadas["tensao"])
print(corrente_de_cada_lampada)

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)

corrente_de_todas_as_lampadas = corrente_de_cada_lampada * lampadas["quantidade"]
corrente_de_todas_as_lampadas

minhas_funcoes.selecionar_disjuntor(corrente_de_todas_as_lampadas)