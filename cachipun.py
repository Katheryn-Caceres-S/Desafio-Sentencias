import random
import sys

opciones = ["piedra", "papel", "tijera"]

if len(sys.argv) != 2:
    print("Uso correcto: python juego.py [piedra|papel|tijera]")
    sys.exit()

jugador = sys.argv[1].lower()


if jugador not in opciones:
    print("Argumento invalido: Debe ser piedra, papel o tijera.")
    sys.exit()

computador = random.choice(opciones)

print(f"Tu jugaste: {jugador}")
print(f"El computador jugó: {computador}")


if jugador == computador:
    print("¡Empate!")
elif (jugador == "piedra" and computador == "tijera") or \
     (jugador == "papel" and computador == "piedra") or \
     (jugador == "tijera" and computador == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")