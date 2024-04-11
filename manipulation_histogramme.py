import numpy as np


def calculer_histogramme(tableau_2d, w):
    max_value = np.max(tableau_2d)

    # Calcul du nombre de bins en fonction de la valeur maximale
    bins = [0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value]

    # Initialisation du tableau pour stocker les histogrammes
    hist_array = np.zeros(((tableau_2d.shape[0] - w + 1) * (tableau_2d.shape[1] - w + 1), len(bins) - 1))

    # Compteur pour suivre la ligne actuelle dans le tableau hist_array
    current_row = 0

    # Parcourir l'image pour calculer l'histogramme pour chaque fenêtre
    for i in range(tableau_2d.shape[0] - w + 1):
        for j in range(tableau_2d.shape[1] - w + 1):
            # Sélectionner la fenêtre de voisinage
            window = tableau_2d[i:i + w, j:j + w]

            # Calculer l'histogramme pour la fenêtre
            hist, _ = np.histogram(window, bins=bins, range=(0, max_value))

            # Stocker l'histogramme dans le tableau
            hist_array[current_row] = hist
            current_row += 1

    return hist_array


def calculer_distance_1(histogramme1, histogramme2):
    """
    Calculer la distance entre deux histogrammes.

    Arguments :
    histogramme1 (numpy.ndarray) : Premier histogramme sous forme de tableau 1D NumPy.
    histogramme2 (numpy.ndarray) : Deuxième histogramme sous forme de tableau 1D NumPy.

    Returns :
    float : La distance entre les deux histogrammes.
    """
    # Vérifier que les histogrammes ont la même longueur
    if len(histogramme1) != len(histogramme2):
        raise ValueError("Les histogrammes doivent avoir la même longueur.")

    # Calculer la distance selon la formule spécifiée
    distance = np.sqrt(np.sum((histogramme1 - histogramme2) ** 2))
    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)
    return float(distance_arrondie)


def calculer_distance_2(histogramme1, histogramme2):
    # Calculer la somme des différences absolues entre les éléments correspondants
    distance = np.sum(np.abs(histogramme1 - histogramme2))

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return float(distance_arrondie)
