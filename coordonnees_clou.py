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
from transformation_geometrique import calculer_reflexion_point
from transformation_geometrique import calculer_rotate_point
from transformation_geometrique import calculer_inclinaison_point

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, direction_inclinaison, angle_inclinaison, axe_reflexion):

    resultats_reflexion = []
    resultats_rotation = []
    resultats_inclinaison = []

    # Application des transformations sur chaque point clé
    for nom, (x, y) in points_clou:
        # Transformation de réflexion
        reflexion = calculer_reflexion_point((x, y), axe_reflexion)
        resultats_reflexion.append((nom, reflexion))

        # Transformation de rotation
        rotation = calculer_rotate_point((x, y), angle_rotation, center_rotation)
        resultats_rotation.append((nom, rotation))

        # Transformation d'inclinaison
        inclinaison = calculer_inclinaison_point((x, y), angle_inclinaison, direction_inclinaison)
        resultats_inclinaison.append((nom, inclinaison))

    return resultats_reflexion, resultats_rotation, resultats_inclinaison