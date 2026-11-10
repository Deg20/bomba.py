import random

print("Bomba activada")
print("Hay 3 cables: 1, 2 y 3")

<<<<<<< HEAD
cable_bueno = random.randint(1, 3)
cable = int(input("Que cable cortas? "))

if cable == cable_bueno:
    print("Has ganado! Bomba desactivada")
else:
    print("BOOM! Has perdido")
=======
cables = ["Rojo", "Azul", "Verde"]
correcto = random.randint(1, 3)

for numero, color in enumerate(cables, start=1):
    print(f"{numero}. {color}")

try:
    eleccion = int(input("\n¿Qué cable eliges? (1, 2 o 3): "))

    if eleccion not in (1, 2, 3):
        print("Esa opción no existe. Fin de la partida.")
    elif eleccion == correcto:
        print("\n✅ ¡Has acertado! Bomba ficticia desactivada. ¡Has ganado!")
    else:
        print("\n💥 ¡BOOM! Has elegido otro cable. Fin del juego.")
except ValueError:
    print("Debes escribir un número. Fin de la partida.")
>>>>>>> parent of 4dfae57 (Bomba)
