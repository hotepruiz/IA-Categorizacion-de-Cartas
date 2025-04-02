from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import FuncionesExtra 
#modelo
model = YOLO("Modelo entrenado/best.pt")
imagen = cv2.imread(f"testhotep.jpeg")

resultados = model(imagen)

# Dibujar cajas
for resultado in resultados:
    for box in resultado.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del bounding box
        conf = box.conf[0].item()  # Confianza
        label = int(box.cls[0].item())  # Clase predicha
        
        # Dibujar bounding box
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 8)
        
        # Etiqueta con clase y confianza
        texto = FuncionesExtra.ClasesANombre(label)
        cv2.putText(imagen, texto, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 0), 5)

# Mostrar imagen con detecciones
FuncionesExtra.MostrarImagen(imagen)