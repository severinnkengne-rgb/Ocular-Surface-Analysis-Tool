import cv2
import numpy as np

def check_image_quality(image_path):
    # Charger l'image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return "Erreur : Image introuvable."

    # 1. Calcul de la netteté (Variance du Laplacien)
    # Un score bas = image floue
    laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()

    # 2. Calcul du contraste (Écart-type de la luminosité)
    contrast = img.std()

    return {
        "Netteté (Laplacian)": round(laplacian_var, 2),
        "Contraste": round(contrast, 2)
    }

# Exemple d'utilisation
# print(check_image_quality("ton_image.jpg"))
