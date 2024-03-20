def calculer_coordonnes_clou(a, b, c, d, e):
    # Calcul des coordonnées selon la paramétrisation
    pt_0 = (-b / 2, c / 2)
    pt_1 = (-b / 2, -c / 2)
    pt_2 = (-b / 2 - d, -a / 2)
    pt_3 = (-b / 2 - d, a / 2)
    pk_0 = (b / 2 + e, 0)
    pk_1 = (b / 2, -c / 2)
    pk_2 = (b / 2, c / 2)
    points = [('pt_0', pt_0), ('pt_1', pt_1), ('pt_2', pt_2), ('pt_3', pt_3), ('pk_2', pk_2), ('pk_0', pk_0),
              ('pk_1', pk_1)]
    return points
