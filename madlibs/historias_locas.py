# concatenar cadenas de caracteres.
# Supongamos que qeremos crear una cadena que diga:
# Dorian Gray mató a su amigo _____

# amigo = "Basil"
#
# print("Dorian Gray mató a su amigo " + amigo)
# print("Dorian Gray mató a su amigo {}".format(amigo))
# print(f"Dorian Gray mató a su amigo {amigo}")  f-string

# Mad Libs (Historias locas)

adj = input("Adjetivo: ")

verbo1 = input("Verbo: ")

verbo2 = input("Verbo: ")

sustantivo_plural = input("Sustantivo (plural): ")

madlib = (f"¡Programar es tan {adj}! Siempre me emociona porque me encanta "
          f"{verbo1} problemas. !Aprende a {verbo2} libremente y podras alcanzar tus {sustantivo_plural}")

print(madlib)