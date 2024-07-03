import random


def adivina_el_numero(x):
    print("===================")
    print("Bienvenido al juego")
    print("===================")
    print("Tu reto es adivinar el numero generado por la computadora.")

    numero_aleatorio = random.randint(1,x)  # Número aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))  # f-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez con un número mayor.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez con un número menor.")

    print(f"¡Felicitaciones! Adivinaste el numero {prediccion} correctamente.")


adivina_el_numero(100)