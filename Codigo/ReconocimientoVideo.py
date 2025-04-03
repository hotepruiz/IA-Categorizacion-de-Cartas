from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import FuncionesExtra 

#modelo
model = YOLO("Modelo entrenado/best.pt")
#camara
cap = cv2.VideoCapture(0) 

while True:
    ret, fotograma = cap.read()
    if not ret:
        break
    
    #----------------------------------------------------------------------------------
    resultados=model.predict(fotograma)

    imgProcesada=FuncionesExtra.DibujarCajas(fotograma, resultados)

    cv2.imshow("pene", imgProcesada)

    #----------------------------------------------------------------------------------
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
        break

cap.release()
cv2.destroyAllWindows()