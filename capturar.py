import mss
import numpy as np
import cv2
import os
import uuid
from pynput import keyboard

PASTA = "dataset/images/train"
os.makedirs(PASTA, exist_ok=True)

sct = mss.MSS()
monitor = sct.monitors[1]

contador = 1

print("C = Salvar print")
print("ESC = Sair")

def on_press(key):
    global contador

    try:
        if key.char == 'c':
            img = np.array(sct.grab(monitor))
            nome = os.path.join(PASTA, f"{uuid.uuid4().hex}.png")
            cv2.imwrite(nome, img)
            print(f"Salvou {nome}")
            contador += 1
    except AttributeError:
        if key == keyboard.Key.esc:
            return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()