
import time
import winsound

#printea el mensaje sobre que la bomba se ha activado
print("💣 Bomba activada...")

#empieza el bucle de la cuenta atras

for segundos in range(10, 0, -1):
    print(f"Explota en {segundos}...")
    winsound.Beep(1000, 200) 
    time.sleep(0.8)

#explota

print("💥 ¡BOOOOM!")
winsound.Beep(200, 1500)    