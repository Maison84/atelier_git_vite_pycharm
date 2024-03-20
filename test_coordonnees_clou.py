from coordonnees_clou import calculer_coordonnes_clou

def test_calculer_coordonnees_clou():
    a = 3
    b = 10
    c = 1
    d = 0.75
    e = 2
    resultat = calculer_coordonnes_clou(a, b, c, d, e)
    attendu = [('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2',
(-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_2', (5.0,
0.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5))]
    assert resultat == attendu