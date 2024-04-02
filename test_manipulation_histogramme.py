

import numpy as np
from manipulation_histogramme import calculer_histogramme,calculer_distance_1,calculer_distance_2
# Test pour vérifier le bon fonctionnement de la fonction calculer_histogramme

def test_calculer_histogramme():
    # Tableau d'entrée
    tableau_2D = np.array([[255, 160, 10, 49],
                            [20, 170, 1, 121],
                            [30, 233, 230, 100],
                            [255, 23, 155, 88]])
    # Taille du carré de voisinage
    w = 3
    # Résultat attendu
    resultat_attendu = np.array([[4, 0, 2, 3],
                                    [3, 2, 2, 2],
                                    [4, 0, 2, 3],
                                    [2, 3, 2, 2]])
    # Appel de la fonction à tester
    resultat_obtenu = calculer_histogramme(tableau_2D, w)
    print(resultat_obtenu)
    # Vérification que le résultat obtenu est égal au résultat attendu
    np.testing.assert_array_equal(resultat_obtenu, resultat_attendu)

def test_calculer_distance1():
    # Les histogrammes fournis
    h1 = np.array([1, 2, 3, 4, 5])
    h2 = np.array([2, 3, 4, 5, 6])

    # La valeur attendue
    valeur_attendue = 2.24

    # Calcul de la distance
    distance_calculee = calculer_distance_1(h1, h2)

    # Vérification que la distance calculée est égale à la valeur attendue
    assert np.array_equal(distance_calculee, valeur_attendue)

def test_calculer_distance2():
    # Les histogrammes fournis
    h1 = np.array([1, 2, 3, 4, 5])
    h2 = np.array([2, 3, 4, 5, 6])

    # La valeur attendue
    valeur_attendue = 5

    # Calcul de la distance
    distance_calculee = calculer_distance_2(h1, h2)

    # Vérification que la distance calculée est égale à la valeur attendue
    assert np.array_equal(distance_calculee, valeur_attendue)