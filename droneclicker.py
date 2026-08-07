from ultralytics import YOLO
import cv2
import pyautogui
import mss
import numpy as np
import time

model = YOLO("runs/detect/train/weights/best.pt")

sct = mss.mss()
monitor = sct.monitors[1]

fps = 5
delay = 1 / fps

while True:
    inicio = time.time()

    img = sct.grab(monitor)

    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    results = model(frame, conf=0.3)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]

            x = int((x1 + x2) / 2)
            y = int((y1 + y2) / 2)

            print(f"Drone detectado: {x}, {y}")

            pyautogui.click(x, y)

    cv2.imshow("YOLO", frame)

    # controla FPS
    tempo_passado = time.time() - inicio
    espera = delay - tempo_passado

    if espera > 0:
        time.sleep(espera)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()