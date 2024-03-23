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

def appliquer_transformation_clou(point_clou, center_rotation, angle_rotation, angle_inclinaison, direction_inclinaison, axe_reflexion):
    # Calcul des coordonnées des points pour chaque transformation
    reflexion = calculer_reflexion_point(point_clou, axe_reflexion)
    rotation = calculer_rotate_point(point_clou, angle_rotation, center_rotation)
    inclinaison = calculer_inclinaison_point(point_clou, angle_inclinaison, direction_inclinaison)
    return [reflexion], [rotation], [inclinaison]

