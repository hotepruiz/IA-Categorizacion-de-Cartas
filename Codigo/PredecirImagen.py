from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import FuncionesExtra 

model = YOLO("Modelo entrenado/best.pt")#Cargar modelo

imagen = cv2.imread(f"jc.jpeg") #ruta para la imagen a predecir

resultados = model(imagen)#Pasarle la imagen a el modelo

# Dibujar cajas
FuncionesExtra.DibujarCajas(imagen, resultados)

# Mostrar imagen con detecciones
FuncionesExtra.MostrarImagen(imagen)