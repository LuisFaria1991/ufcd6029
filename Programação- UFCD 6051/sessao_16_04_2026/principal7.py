# ciclo principal

while True:
    # dados de entrada
    sensor_humidade = 5
    planta = 2
    temporizador = 75 

    # processamento
    if sensor_humidade < 10 and planta == 2 and temporizador > 72:
        liga_rega = True
    else:
        liga_rega = False