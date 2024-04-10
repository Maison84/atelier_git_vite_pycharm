from PIL import Image
import numpy as np


def appliquer_rgb_to_gry(image_couleur, image_niveaux_de_gris):
    '''
        Description :
            Transforme une image en couleur en une nouvelle image en niveaux de gris

        Arguments :
            Une string : le chemin de l'image en couleur à transformer
            Une string : le chemin de l'image en gris à transformer

        Retourne :
            La fonction ne retourne rien mais sauvegarde l'image en niveaux de gris au chemin spécifier
    '''
    # Ouvrir l'image en couleur
    image_couleur = Image.open('image_couleur.jpg')

    # Obtenir les dimensions de l'image
    largeur, hauteur = image_couleur.size

    # Créer une nouvelle image en niveaux de gris
    image_gris = Image.new('L',(largeur, hauteur))

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
    image_gris.save('image_niveaux_de_gris.jpg')

    # Affichage d'un message pour confirmer la sauvegarde
    print("Image en niveaux de gris sauvegardée avec succès.")


def appliquer_transformation_1(image_niveaux_gris):
    '''
        Description :
            Prend une image en niveaux de gris sous forme d'un tableau et applique une transformation et extraire des caractéristiques de l'image

        Arguments :
            numpy.ndarray : un tableau 2D NumPy représentant une image en niveaux de gris

        Retourne :
            numpy.ndarray : un tableau 2D NumPy résultant de la transformation appliquée
    '''
    # Définir la taille de l'image
    hauteur, largeur = image_niveaux_gris.shape

    # Créer un tableau pour stocker le résultat de la transformation
    resultat = np.zeros((hauteur, largeur), dtype=np.uint8)

    # Parcourir chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # Vérifier si le pixel est sur le bord de l'image
            if y == 0 or y == hauteur - 1 or x == 0 or x == largeur - 1:
                # Si oui, attribuer la valeur de zéro au pixel résultant
                resultat[y, x] = 0
            else:
                # Récupérer la valeur de gris du pixel central
                g_c = image_niveaux_gris[y, x]

                # Initialiser le motif binaire
                motif_binaire = ""

                # Coordonnées des voisins dans l'ordre de suivi
                voisins_coords = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x + 1),
                                  (y + 1, x + 1), (y + 1, x), (y + 1, x - 1), (y, x - 1)]

                # Parcourir les voisins du pixel central dans l'ordre de suivi
                for voisin_y, voisin_x in voisins_coords:
                    # Récupérer la valeur de gris du voisin
                    g_v = image_niveaux_gris[voisin_y, voisin_x]

                    # Comparer avec la valeur du pixel central
                    if g_v >= g_c:
                        motif_binaire += '1'
                    else:
                        motif_binaire += '0'

                # Convertir le motif binaire en valeur décimale
                valeur_decimale = int(motif_binaire, 2)

                # Assigner la valeur du pixel résultant
                resultat[y, x] = valeur_decimale

    return resultat


def appliquer_transformation_2(image_gris, rayon):
    '''
        Description :
            Transforme les données visuelles complexes d'une image en ensemble de caractéristiques

        Arguments :
            numpy.ndarray : un tableau 2D NumPy représentant une image en niveaux de gris
            int : un entier spécifiant le rayon du voisinage à considérer

        Retourne :
            numpy.ndarray : un tableau 2D NumPy résultant de la transformation appliquée
    '''
    # Définir la taille de l'image
    hauteur, largeur = image_gris.shape

    # Créer un tableau pour stocker le résultat de la transformation
    resultat = np.zeros((hauteur, largeur), dtype=np.float64)

    # Parcourir chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # Vérifier si le pixel est sur le bord de l'image
            if x < rayon or x >= largeur - rayon or y < rayon or y >= hauteur - rayon:
                # Si oui, attribuer la valeur de zéro au pixel résultant
                resultat[y, x] = 0
            else:
                # Calculer la valeur de sortie O(x, y) pour chaque pixel
                somme_logarithmique = np.log10(
                    1 + abs(image_gris[y, x + rayon] - 2 * image_gris[y, x] + image_gris[y, x - rayon]))
                somme_logarithmique += np.log10(
                    1 + abs(image_gris[y + rayon, x] - 2 * image_gris[y, x] + image_gris[y - rayon, x]))
                somme_logarithmique += np.log10(
                    1 + abs(image_gris[y - rayon, x + rayon] - 2 * image_gris[y, x] + image_gris[y + rayon, x - rayon]))

                # Assigner la valeur du pixel résultant, en prenant soin de ne pas dépasser 255
                resultat[y, x] = min(somme_logarithmique, 255)

    # Convertir la matrice résultante de float à int
    resultat = resultat.astype(np.uint8)

    return resultat

