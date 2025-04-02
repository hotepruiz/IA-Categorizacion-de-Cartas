import cv2
import matplotlib.pyplot as plt

def MostrarImagen(imagen):
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
    else:
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir a RGB
        plt.imshow(imagen_rgb)
        plt.axis("off")  # Ocultar ejes
        plt.show()

def ClasesANombre(NumeroClase: int):
    NombreClases = [
    '10 de treboles', '10 de diamantes', '10 de corazones', '10 de espadas',
    '2 de treboles', '2 de diamantes', '2 de corazones', '2 de espadas',
    '3 de treboles', '3 de diamantes', '3 de corazones', '3 de espadas',
    '4 de treboles', '4 de diamantes', '4 de corazones', '4 de espadas',
    '5 de treboles', '5 de diamantes', '5 de corazones', '5 de espadas',
    '6 de treboles', '6 de diamantes', '6 de corazones', '6 de espadas',
    '7 de treboles', '7 de diamantes', '7 de corazones', '7 de espadas',
    '8 de treboles', '8 de diamantes', '8 de corazones', '8 de espadas',
    '9 de treboles', '9 de diamantes', '9 de corazones', '9 de espadas',
    'A de treboles', 'A de diamantes', 'A de corazones', 'A de espadas',
    'J de treboles', 'J de diamantes', 'J de corazones', 'J de espadas',
    'K de treboles', 'K de diamantes', 'K de corazones', 'K de espadas',
    'Q de treboles', 'Q de diamantes', 'Q de corazones', 'Q de espadas'
]
    
    return NombreClases[NumeroClase]
    

