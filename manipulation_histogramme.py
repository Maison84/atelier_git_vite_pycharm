import numpy as np


def calculer_histogramme(tableau_2D, w):
    max_val = 255
    # Créer un tableau pour stocker les histogrammes de chaque fenêtre
    # La taille du tableau est réduite de w-1 pour chaque dimension
    hist_array = np.zeros((tableau_2D.shape[0] - w + 1, tableau_2D.shape[1] - w + 1, 4))

    # Parcourir l'image pour calculer l'histogramme pour chaque fenêtre
    for i in range(hist_array.shape[0]):
        for j in range(hist_array.shape[1]):
            # Sélectionner la fenêtre de voisinage
            window = tableau_2D[i:i + w, j:j + w]

            # Calculer l'histogramme pour la fenêtre
            hist, _ = np.histogram(window, bins=[0, 64, 128, 192, max_val + 1], range=(0, max_val))

            # Stocker l'histogramme dans le tableau
            hist_array[i, j] = hist

    # Redimensionner le tableau pour qu'il soit 2D
    hist_array_redimensionne = hist_array.reshape(-1, 4)

    return hist_array_redimensionne


def calculer_distance_1(histogramme1, histogramme2):
    # Calculer la différence au carré entre les éléments correspondants des deux histogrammes
    difference_carre = (histogramme1 - histogramme2) ** 2

    # Somme des différences au carré
    somme_diff_carre = np.sum(difference_carre)

    # Calculer la racine carrée de la somme pour obtenir la distance
    distance = np.sqrt(somme_diff_carre)

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return distance_arrondie


def calculer_distance_2(histogramme1, histogramme2):
    # Calculer la somme des différences absolues entre les éléments correspondants
    distance = np.sum(np.abs(histogramme1 - histogramme2))

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return distance_arrondie
