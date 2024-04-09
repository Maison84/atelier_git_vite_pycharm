import numpy as np
import matplotlib as plt
from manipulation_histogramme import calculer_distance_1
from traitement_image import appliquer_transformation_2
from PIL import Image



def regrouper_points(data_hist, k=5, max_iterations=50):
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




    return indices_groupes


