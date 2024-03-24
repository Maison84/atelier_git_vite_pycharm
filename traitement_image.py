from PIL import Image
import numpy as np
def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):
    # Ouvrir l'image en couleur
    image_couleur = Image.open(r"C:\Users\maiso\Documents\ETS\H24\INF136\INF136 - H2024 - Projet\image_couleur.jpg")

    # Obtenir les dimensions de l'image
    largeur, hauteur = image_couleur.size

    # Créer une nouvelle image en niveaux de gris
    image_gris = Image.new("L", (largeur, hauteur))

    # Parcourir chaque pixel de l'image en couleur et calculer la moyenne des composantes RVB
    for y in range(hauteur):
        for x in range(largeur):
            # Obtenir les valeurs RVB du pixel
            r, g, b = image_couleur.getpixel((x, y))

            # Calculer la moyenne des composantes RVB
            niveau_gris = (r + g + b) // 3

            # Définir la valeur de pixel de l'image en niveaux de gris
            image_gris.putpixel((x, y), niveau_gris)

    # Sauvegarder l'image en niveaux de gris
    image_gris.save(r"C:\Users\maiso\Documents\ETS\H24\INF136\INF136 - H2024 - Projet\image_niveaux_de_gris.jpg")

    # Affichage d'un message pour confirmer la sauvegarde
    print("Image en niveaux de gris sauvegardée avec succès.")


