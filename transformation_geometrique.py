import numpy as np

def calculer_reflexion_point(point, axe):
    '''
        Description :
            Applique une réflexion à un point par rapport à un axe spécifié

        Arguments :
            Un tuple : coordonnées du point à réflechir
            Une string : axe de refléxion

        Retourne :
            Un tuple des nouvelles coordonnées de point après réflexion
    '''
    x, y = point
    if axe == 'x':
        return (x, -y)
    elif axe == 'y':
        return (-x, y)

def calculer_rotate_point(point, angle, center=(0, 0)):
    '''
            Description :
                Prend un point dans le plan cartésien et le fait pivoter autour d'un point central donné d'un certain angle.

            Arguments :
                Un tuple : coordonnées du point à faire pivoter
                Un float : angle de rotation en degrés
                Un tuple : coordonnées du centre de rotation

            Retourne :
                Un tuple des nouvelles coordonnées du point après rotation.
    '''
    angle_rad = np.radians(angle)
    sin_angle = np.sin(angle_rad)
    cos_angle = np.cos(angle_rad)

    x_translated = point[0] - center[0]
    y_translated = point[1] - center[1]

    x_rotated = x_translated * cos_angle - y_translated * sin_angle
    y_rotated = x_translated * sin_angle + y_translated * cos_angle

    x_final = x_rotated + center[0]
    y_final = y_rotated + center[1]

    return round(x_final, 2), round(y_final, 2)

def calculer_inclinaison_point(point, angle, direction):
    '''
        Description :
            Applique une transformation d'inclinaison sur un point.

        Arguments :
            Un tuple : coordonnées du point à incliner
            Un float : angle d'inclinaison
            Une string : direction de l'inclinaison

        Retourne :
            Un tuple réprensentant les nouvelles coordonnées du point après l'inclinaison.
    '''
    m = np.tan(np.radians(angle))  # Calcul de la tangente de l'angle d'inclinaison
    print(m)
    if direction == 'x':
        # Cisaillement horizontal
        x = point[0] + (m * point[1])
        y = point[1]
    elif direction == 'y':
        # Cisaillement vertical
        x = point[0]
        y = m * point[0] + point[1]
    return round(x, 2), round(y, 2)


