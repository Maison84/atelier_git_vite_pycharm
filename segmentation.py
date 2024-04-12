import numpy as np
from manipulation_histogramme import calculer_distance_1

def regrouper_points(data, k=2, max_iterations=50):
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
    # Initialisation des centres de groupe de manière aléatoire
    val_aleatoire = np.random.choice(len(data), 2, replace=False)
    centres = data[val_aleatoire]
    centres = np.array([[0,2,7,0], [6,3,0,0]])
    # Initialisation de l'affectation de groupe
    affectations = []

    # Boucle principale de l'algorithme
    for i in range(max_iterations):
        # Calcul des distances entre chaque point et chaque centre de groupe
        distances = np.array([[calculer_distance_1(point, centre) for centre in centres]for point in data])

        # Attribution de chaque point au groupe avec le centre le plus proche
        nouveaux_centres = np.argmin(distances, axis=1)

        # Vérification de la convergence
        if np.array_equal(affectations, nouveaux_centres):
            break

        affectations = nouveaux_centres

        # Mise à jour des centres de groupe
        for i in range(k):
            groupe_de_points = data[affectations == i]
            if len(groupe_de_points) > 0:
                centres[i] = np.mean(groupe_de_points, axis=0)


    return affectations






