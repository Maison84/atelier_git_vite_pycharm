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