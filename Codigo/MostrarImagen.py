import cv2
import matplotlib.pyplot as plt
import FuncionesExtra #Mi archivo


# Archivo de clases
class_names = ['10c', '10d', '10h', '10s', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', 
               '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', 
               '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 
               'Ac', 'Ad', 'Ah', 'As', 'Jc', 'Jd', 'Jh', 'Js', 'Kc', 'Kd', 'Kh', 'Ks', 
               'Qc', 'Qd', 'Qh', 'Qs']


nombreImagen="000554394_jpg.rf.8be18f32226fb0d2208dddd4349077ba"


imagen = cv2.imread(f"train/images/{nombreImagen}.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

with open(f'train/labels/{nombreImagen}.txt', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()


labels= []
for line in lines:
    valores = line.strip().split() 
    tupla = (int(valores[0]), float(valores[1]), float(valores[2]), float(valores[3]), float(valores[4]))
    labels.append(tupla)

# Tamaño de la imagen
h, w, _ = imagen.shape

# Dibujar las cajas en la imagen
for label in labels:
    class_id, x_center, y_center, width, height = label
    x1 = int((x_center - width / 2) * w)
    y1 = int((y_center - height / 2) * h)
    x2 = int((x_center + width / 2) * w)
    y2 = int((y_center + height / 2) * h)

    # Dibujar rectángulo
    cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 0, 250), 2)
    
    # Etiqueta con el nombre de la carta
    class_name = class_names[class_id]
    cv2.putText(imagen, class_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 250), 2)

FuncionesExtra.MostrarImagen(imagen)