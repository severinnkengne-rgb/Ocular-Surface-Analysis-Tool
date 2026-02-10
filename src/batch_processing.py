import cv2
import os
import csv

def process_all_dataset(gland_folder, eyelid_folder, output_csv):
    # 1. Créer le fichier de résultats
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Image_Name", "Atrophy_Percentage"])

        # 2. Lister les fichiers dans le dossier des glandes
        images = os.listdir(gland_folder)
        
        for img_name in images:
            gland_path = os.path.join(gland_folder, img_name)
            eyelid_path = os.path.join(eyelid_folder, img_name)

            # Vérifier si le masque de paupière correspondant existe
            if os.path.exists(eyelid_path):
                gland_mask = cv2.imread(gland_path, cv2.IMREAD_GRAYSCALE)
                eyelid_mask = cv2.imread(eyelid_path, cv2.IMREAD_GRAYSCALE)

                # Calcul des surfaces
                area_eyelid = cv2.countNonZero(eyelid_mask)
                area_glands = cv2.countNonZero(gland_mask)

                if area_eyelid > 0:
                    atrophy = (1 - (area_glands / area_eyelid)) * 100
                    writer.writerow([img_name, round(atrophy, 2)])
    
    print(f"Analyse terminée. Résultats sauvegardés dans {output_csv}")

# Exemple d'appel :
# process_all_dataset('Meibomian Gland label', 'eyelid labels', 'resultats_atrophie.csv')
