import cv2
import numpy as np

def segment_glands(image_path):
    # 1. Charger l'image en niveaux de gris
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None: return "Image non trouvée."

    # 2. Appliquer un flou Gaussien pour réduire le "bruit" (les grains sur l'image)
    blur = cv2.GaussianBlur(img, (5,5), 0)

    # 3. Segmentation d'Otsu : calcule le seuil optimal automatiquement
    # Elle sépare les pixels en deux groupes : les Glandes et le Fond
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh

# Ce script transforme une image complexe en une carte binaire (Noir et Blanc)
