import numpy as np
from traitement_image import appliquer_transformation_1, appliquer_transformation_2


def test_appliquer_transformation_1():
    tableau_fourni_1_a = np.array([
        [2, 5, 3, 9, 15],
        [6, 7, 9, 1, 5],
        [3, 8, 4, 2, 9],
        [2, 3, 5, 8, 2],
        [1, 2, 3, 2, 1]
    ], dtype=np.uint8)

    # Tableau NumPy attendu
    tableau_attendu_1_a = np.array([
        [0, 0, 0, 0, 0],
        [0, 20, 32, 255, 0],
        [0, 32, 205, 191, 0],
        [0, 248, 144, 32, 0],
        [0, 0, 0, 0, 0]
    ], dtype=np.uint8)

    # Appliquer la transformation
    tableau_resultat_1_a = appliquer_transformation_1(tableau_fourni_1_a)
    print(tableau_resultat_1_a)
    # Vérifier si le résultat correspond au tableau attendu
    assert np.array_equal(tableau_resultat_1_a, tableau_attendu_1_a)

def test_appliquer_transformation_1_b():
    tableau_fourni_1_b = np.array([
        [88, 20, 56, 49, 145, 123],
        [60, 17, 99, 121, 55, 56],
        [80, 8, 45, 100, 99, 30],
        [255, 23, 155, 88, 12, 78],
        [100, 200, 23, 82, 155, 254]
    ], dtype=np.uint8)

    # Tableau NumPy attendu
    tableau_attendu_1_b = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 251, 24, 32, 119, 0],
        [0, 255, 124, 66, 129, 0],
        [0, 191, 2, 105, 255, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=np.uint8)

    # Appliquer la transformation
    tableau_resultat_1_b = appliquer_transformation_1(tableau_fourni_1_b)
    print(tableau_resultat_1_b)
    # Vérifier si le résultat correspond au tableau attendu
    assert np.array_equal(tableau_resultat_1_b, tableau_attendu_1_b)

def test_transformation_2_a():
    # Tableau NumPy fourni
    tableau_fourni_2_a = np.array([
        [88, 102, 133, 49, 145, 123],
        [14, 100, 200, 121, 55, 56],
        [40, 101, 92, 100, 99, 30],
        [255, 23, 155, 88, 12, 78],
        [100, 200, 23, 82, 155, 254]
    ], dtype=np.uint8)

    # Tableau NumPy attendu
    tableau_attendu_2_a = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 3, 6, 3, 6, 0],
        [0, 6, 5, 3, 5, 0],
        [0, 7, 5, 3, 6, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=np.uint8)

    # Appliquer la transformation avec un rayon de 1
    tableau_resultat_2_a = appliquer_transformation_2(tableau_fourni_2_a, 1)

    print(tableau_resultat_2_a)
    # Vérifier si le résultat correspond au tableau attendu
    assert np.array_equal(tableau_resultat_2_a, tableau_attendu_2_a)

def test_transformation_2_b():
    # Tableau NumPy fourni
    tableau_fourni_2_b = np.array([
        [88, 102, 133, 49, 145, 123],
        [14, 100, 200, 121, 55, 56],
        [40, 101, 92, 100, 99, 30],
        [255, 23, 155, 88, 12, 78],
        [100, 200, 23, 82, 155, 254]
    ], dtype=np.uint8)

    # Tableau NumPy attendu
    tableau_attendu_2_b = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=np.uint8)

    # Appliquer la transformation avec un rayon de 2
    tableau_resultat_2_b = appliquer_transformation_2(tableau_fourni_2_b, 2)

    print(tableau_resultat_2_b)
    # Vérifier si le résultat correspond au tableau attendu
    assert np.array_equal(tableau_resultat_2_b, tableau_attendu_2_b)