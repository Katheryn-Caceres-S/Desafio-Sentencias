import random
import sys


if len(sys.argv) != 2:
    print ("python ejemplo.py [ingreso]")

opciones = sys.argv[1]
opciones = ["piedra", "papel", "tijeras"]

while True:
    jugador = input ("elije piedra, papel o tijeras o escribe 'salir' ")

    if jugador =="salir":
        print ("juego terminado!!")
        break

    if jugador not in opciones:
        print ("opcion no valida..")
        continue

  computador = random.choices(opciones)

  print(f"el jugador eligio {jugador}")
  print(f"el jugador eligio {computador}")


  if jugador == computador:
    print ("empate!...")

  elif jugador == "piedra" and computador ==" tijeras":
    print("ganaste")

  elif jugador == "papel" and computador ==" piedra":
    print ("ganaste")

  elif jugador == "tijeras" and computador =="papel":
    print ("ganaste")

  else:
    print ("perdiste!!") 