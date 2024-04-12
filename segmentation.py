import numpy as np
from manipulation_histogramme import calculer_distance_1

def regrouper_points(data_hist, k=5, max_iterations=50):
    '''
        Description :
            Diviser un ensemble de points dans un plan 2D en un nombre défini de groupe

        Arguments :
            numpy.ndarray : un tableau 2D numpy représentant l'ensemble de données à partitionner
            int : le nombre de groupes à identifier dans l'ensemble de données
            int : le nombre de maximal d'itérations que l'algorithme exécutera, la valeur par défaut est 50

        Retourne :
            numpy.ndarray : un tableau 1D où chaque élément correspond à l'indice du centre le plus proche pour chaque point de l'ensemble de données
    '''
    # Générer une permutation aléatoire des indices
    indices_permutes = np.random.permutation(data_hist.shape[0])

    # Sélectionner les k premiers indices permutés comme centres initiaux
    centres_initiaux = data_hist[indices_permutes[:k]]

    distances = np.zeros((data_hist.shape[0], centres_initiaux.shape[0]))
    for i, hist_point in enumerate(data_hist):
        for j, hist_centroid in enumerate(centres_initiaux):
            distances[i, j] = calculer_distance_1(hist_point, hist_centroid)

    indices_groupes = np.argmin(distances, axis=1)

    return indices_groupes