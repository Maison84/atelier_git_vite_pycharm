from transformation_geometrique import calculer_reflexion_point

def test_calculer_reflexion_point_1():

  point = (2, 4)
  axe = 'x'

  resultat = calculer_reflexion_point(point, axe)

  attendu = (2, -4)

  assert resultat == attendu, f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."


def test_calculer_reflexion_point_2():

  point = (2, 4)
  axe = 'y'

  resultat = calculer_reflexion_point(point, axe)

  attendu = (-2, 4)

  assert resultat == attendu, f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."


from transformation_geometrique import calculer_rotate_point

def test_rotate_point():
    point_attendu = (-0.27, 4.46)
    assert calculer_rotate_point((2, 4), 30) == point_attendu, f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."


from transformation_geometrique import calculer_inclinaison_point

def test_calculer_inclinaison_point_1():
    point = (2, 4)
    angle = 5
    direction = 'x'
    result = calculer_inclinaison_point(point, angle, direction)
    expected = (2.35, 4.0)
    assert result == expected,f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."

def test_calculer_inclinaison_point_2():
    point = (2, 4)
    angle = 5
    direction = 'y'
    result = calculer_inclinaison_point(point, angle, direction)
    expected = (2.0, 4.17)
    assert result == expected, f"Échec du test : le résultat {resultat} ne correspond pas aux valeurs attendues {attendu}."