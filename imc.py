import sys

if len(sys.argv) != 3:
    print("Uso correcto: python imc.py [peso] [altura]")
    sys.exit()

try:
    peso = float(sys.argv[1])
    altura = float(sys.argv[2])
except ValueError:
    print("Error: asegúrate de que el peso y la altura sean números.")
    sys.exit()

imc = peso / (altura ** 2)

print(f"Su peso es: {peso} kg. y su altura es: {altura} metros")
print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
  print("La clasificación OMS es Bajo Peso")

elif imc >= 18.5 and imc <25:
  print ("La clasificación OMS es Adecuado")

elif imc >= 25 and imc < 30:
  print ("La clasificación OMS es Sobrepeso")

elif imc >= 30 and imc < 35:
  print ("La clasificación OMS es Obesidad Grado I")  

elif imc >= 35 and imc < 40:
  print ("La clasificación OMS es Obesidad Grado II")  

elif imc >40 :
  print ("La clasificación OMS es Obesidad Grado III")  
  

else:
  print("hola")