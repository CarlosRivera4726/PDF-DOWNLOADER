import keyboard
import pyperclip
import time 
import os

# Lista para almacenar lo que se copia en el portapapeles
copied_data = []
continueExec = True

def on_key_event(event):
    global copied_data
    
    while True:
        # Comprobar si algo se ha copiado al portapapeles (Ctrl + C)
        if keyboard.is_pressed('ctrl+c'):
            # Obtener el contenido del portapapeles y añadirlo a la lista
            time.sleep(0.5)
            copied_text = pyperclip.paste()
            if('https://www.siisa.com.co/ords/' in copied_text):
                copied_data.append(copied_text)
                os.system('cls')
                for data in set(copied_data):
                    print(f"'{data}',")
        # Comprobar si se presionó la combinación de teclas de salida (Ctrl + Shift + B)
        if keyboard.is_pressed('ctrl+shift+b'):
            # Detener la escucha y salir del bucle
            continueExec = False
            print("Deteniendo la aplicación...")
            break

# Registrar el controlador de eventos para la combinación de teclas
keyboard.hook(on_key_event)

while True:
    pass
# Imprimir los datos copiados


