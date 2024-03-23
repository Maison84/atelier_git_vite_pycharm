from PIL import open, size, save, getpixel

def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):
    moyenne = 0
    i = open("image.png")
    (largeur, hauteur) = i.size
    i.save(chemin_image_couleur/image_couleur.png)
    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = i.getpixel((x, y))
            moyenne += (rouge + vert + bleu) // 3
            i[x][y] = moyenne, moyenne, moyenne
            i.save(chemin_sauvegarde_gris/image_gris.png)

    return None