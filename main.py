from detector import DroneDetector

detector = DroneDetector()

while True:
    frame = capturar_tela()

    drones = detector.detect(frame)

    for drone in drones:
        print("Drone encontrado:", drone)