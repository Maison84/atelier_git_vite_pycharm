from PIL import Image
import numpy as np

chemin_sauvegarde_gris = "image_niveaux_de_gris.jpg"
chemin_image_couleur = "image_couleur.png"
def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):
    # Ouvrir l'image en couleur
    image_couleur = Image.open(chemin_image_couleur)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image_couleur.size

    # Créer une nouvelle image en niveaux de gris
    image_gris = Image.new((largeur, hauteur))

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
    image_gris.save(chemin_sauvegarde_gris)

    # Affichage d'un message pour confirmer la sauvegarde
    print("Image en niveaux de gris sauvegardée avec succès.")

appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris)

def appliquer_transformation_1(image_gris):
