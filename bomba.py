import random

# Minijuego ficticio: el cable correcto se elige al azar.
print("💣 ¡Bomba de mentira activada!")
print("Tienes 3 cables. Elige uno para desactivar el simulador:\n")

<<<<<<< Updated upstream
cables = ["Rojo", "Azul", "Verde"]
correcto = random.randint(1, 3)
=======
#printea el mensaje sobre que la bomba se ha activado
print(" Bomba activada...")
>>>>>>> Stashed changes

for numero, color in enumerate(cables, start=1):
    print(f"{numero}. {color}")

try:
    eleccion = int(input("\n¿Qué cable eliges? (1, 2 o 3): "))

<<<<<<< Updated upstream
    if eleccion not in (1, 2, 3):
        print("Esa opción no existe. Fin de la partida.")
    elif eleccion == correcto:
        print("\n✅ ¡Has acertado! Bomba ficticia desactivada. ¡Has ganado!")
    else:
        print("\n💥 ¡BOOM! Has elegido otro cable. Fin del juego.")
except ValueError:
    print("Debes escribir un número. Fin de la partida.")
=======
#explota

print("¡Explosión!")
winsound.Beep(200, 1500)    
>>>>>>> Stashed changes
