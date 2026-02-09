import cv2
import numpy as np

def calculate_atrophy(gland_mask_path, eyelid_mask_path):
    # 1. Charger les masques (images en noir et blanc)
    # gland_mask : extrait de ton dossier 'Meibomian Gland label'
    # eyelid_mask : extrait de ton dossier 'eyelid labels'
    gland_mask = cv2.imread(gland_mask_path, cv2.IMREAD_GRAYSCALE)
    eyelid_mask = cv2.imread(eyelid_mask_path, cv2.IMREAD_GRAYSCALE)

    if gland_mask is None or eyelid_mask is None:
        return "Erreur de lecture des fichiers."

    # 2. Calculer les surfaces (compter les pixels blancs)
    area_eyelid = cv2.countNonZero(eyelid_mask)
    area_glands = cv2.countNonZero(gland_mask)

    # 3. Formule mathématique de l'atrophie
    # Atrophie = (Surface Paupière - Surface Glandes) / Surface Paupière
    atrophy_ratio = (1 - (area_glands / area_eyelid)) * 100

    return round(atrophy_ratio, 2)

# Exemple d'usage :
# score = calculate_atrophy('chemin/glande.png', 'chemin/paupiere.png')
# print(f"Taux d'atrophie : {score}%")
