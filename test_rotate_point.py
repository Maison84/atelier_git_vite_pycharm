from transformation_geometrique import calculer_rotate_point
def test_rotate_point():
    point_attendu = (-0.27, 4.46)
    assert calculer_rotate_point((2, 4), 30) == point_attendu, f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."