import numpy as np


def calculer_reflexion_point(point, axe):
    x, y = point
    if axe == 'x':
        y_prime = -y
        return x, y_prime
    elif axe == 'y':
        x_prime = -x
        return x_prime, y

def calculer_rotate_point(point, angle, center=(0, 0)):
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
    m = np.tan(np.radians(angle))  # Calcul de la tangente de l'angle d'inclinaison
    if direction == 'x':
        # Cisaillement horizontal
        x_prime = point[0] + (m * point[1])
        y_prime = point[1]
    elif direction == 'y':
        # Cisaillement vertical
        x_prime = point[0]
        y_prime = m * point[0] + point[1]
    return round(x_prime, 2), round(y_prime, 2)