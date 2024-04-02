import numpy as np
from manipulation_histogramme import calculer_distance_1


def regrouper_points(data, k, max_iterations=50):
    # Initialiser les centres des groupes de manière aléatoire
    centers = data[np.random.choice(len(data), k, replace=False)]

    # Répéter jusqu'à convergence ou atteindre le nombre maximal d'itérations
    for _ in range(max_iterations):
        # Assigner chaque point au groupe dont le centre est le plus proche
        distances = np.array([[calculer_distance_1(point, center) for center in centers] for point in data])
        labels = np.argmin(distances, axis=1)

        # Mettre à jour les centres des groupes
        for i in range(k):
            cluster_points = data[labels == i]
            if len(cluster_points) > 0:
                centers[i] = np.mean(cluster_points, axis=0)

    # Renvoyer les affectations de groupe pour chaque point
    return labels