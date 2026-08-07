from ultralytics import YOLO
import cv2
import numpy as np
import mss

model = YOLO("runs/detect/train/weights/best.pt")

sct = mss.mss()

# monitor principal
monitor = sct.monitors[1]

while True:
    screenshot = np.array(sct.grab(monitor))

    # BGRA -> BGR
    frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    results = model(frame, conf=0.5)

    annotated = results[0].plot()

    cv2.imshow("Egg Inc Detector", annotated)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()