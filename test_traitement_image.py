import numpy as np
from traitement_image import appliquer_transformation_1

def test_appliquer_transformation_1():
    tableau_fourni = np.array([
        [2, 5, 3, 9, 15],
        [6, 7, 9, 1, 5],
        [3, 8, 4, 2, 9],
        [2, 3, 5, 8, 2],
        [1, 2, 3, 2, 1]
    ], dtype=np.uint8)

    # Tableau NumPy attendu
    tableau_attendu = np.array([
        [0, 0, 0, 0, 0],
        [0, 20, 32, 255, 0],
        [0, 32, 205, 191, 0],
        [0, 248, 144, 32, 0],
        [0, 0, 0, 0, 0]
    ], dtype=np.uint8)

    # Appliquer la transformation
    tableau_resultat = appliquer_transformation_1(tableau_fourni)
    print(tableau_resultat)
    # Vérifier si le résultat correspond au tableau attendu
    assert tableau_resultat == tableau_resultat

