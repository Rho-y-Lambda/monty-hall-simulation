import random

numero_de_simulaciones = 100000

aciertos_si_nunca_cambias = 0
aciertos_si_siempre_cambias = 0
aciertos_si_a_veces_cambias = 0

def determinar_si_ganas(puerta_elegida, hay_cambio):

    puerta_ganadora = True
        
    if puerta_elegida == puerta_ganadora and hay_cambio:
        ganas = False
    elif puerta_elegida == puerta_ganadora and not hay_cambio:
        ganas = True
    elif not puerta_elegida == puerta_ganadora and hay_cambio:
        ganas = True
    elif not puerta_elegida == puerta_ganadora and not hay_cambio:
        ganas = False

    return ganas

for _ in range(numero_de_simulaciones):

    # preparar las puertas
    puertas = [False, True, False]
    random.shuffle(puertas)

    # Tú eliges una puerta al azar
    puerta_elegida = random.choice(puertas)

    # Monty Hall quita una puerta sin premio
    puertas.remove(False)

    # determinar si ganas cuando:

    #   a) Nunca cambias
    hay_cambio = False
    if determinar_si_ganas(puerta_elegida, hay_cambio):
        aciertos_si_nunca_cambias += 1

    #   b) Siempre cambias
    hay_cambio = True
    if determinar_si_ganas(puerta_elegida, hay_cambio):
        aciertos_si_siempre_cambias += 1

    #   c) A veces cambias
    hay_cambio = random.choice([True, False])
    if determinar_si_ganas(puerta_elegida, hay_cambio):
        aciertos_si_a_veces_cambias += 1


print(f'Si nunca cambias: {aciertos_si_nunca_cambias/numero_de_simulaciones*100}%')
print(f'Si siempre cambias: {aciertos_si_siempre_cambias/numero_de_simulaciones*100}%')
print(f'Si a veces cambias: {aciertos_si_a_veces_cambias/numero_de_simulaciones*100}%')
