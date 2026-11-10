import random

print("Bomba activada")
print("Hay 3 cables: 1, 2 y 3")

cable_bueno = random.randint(1, 3)
cable = int(input("Que cable cortas? "))

if cable == cable_bueno:
    print("Has ganado! Bomba desactivada")
else:
    print("BOOM! Has perdido")
