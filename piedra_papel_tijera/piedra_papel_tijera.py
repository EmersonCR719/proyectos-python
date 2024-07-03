import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()

    computadora = random.choice(["pi", "pa", "ti"])

    if  usuario == computadora:
        return f"!Empate¡ La computadora escogió {computadora}"

    if  gano_el_jugador(usuario, computadora):
        return f"!Ganaste¡ La computadora escogió {computadora}"

    return f"!Perdiste¡ La computadora escogió {computadora}"


def gano_el_jugador(jugador, oponente):
    # Retorna True (Verdadero) si gana el jugador
    # Piedra gana a tijera (pi > ti)
    # Tijera gana a papel (ti > pa)
    # Papel gana a piedra (pa > pi)

    if ((jugador == 'pi' and oponente == 'ti') or
            (jugador == 'ti' and oponente == 'pa') or
            (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())