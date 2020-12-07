import pygame


class AnimateSprite(pygame.sprite.Sprite):
    images = []

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"./assets/Idle__000.png")
        self.image = pygame.transform.scale(self.image, (70, 150))
        self.current_image = 0
        self.animate = False

    def start_animation(self):
        self.animate = True

    # definir une methode qui permet d'animer le sprite
    def animation(self, type_move, direction, loop=False):

        if self.animate:
            self.images = dictionnaire["ninja"][type_move]
            if type_move == 'Idle':
                scale = (70, 150)
            else:
                scale = (100, 150)
            self.current_image += 0.05
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animate = False
            self.image = self.images[int(self.current_image)]
            self.image = pygame.transform.scale(self.image, scale)
            if direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)


# definir une fonction qui charge les images d'animation
def load_animation_images(spriteName):
    # creation de liste qui va contenir toutes les images chargées
    images = []

    # recuperer le chemin des images à charger
    path = f"./assets/ninja/{spriteName}"
    # faire une boucle pour recuperer les images dans le dossiers
    for numero_image in range(10):
        image_path = path + "__00" + str(numero_image) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu des images dans le jeux
    return images


# dictionnaire des differentes valeurs
dictionnaire = {"ninja": {"Idle": load_animation_images("Idle"),
                          "Run": load_animation_images("Run"),
                          "Jump": load_animation_images("Jump"),
                          "Throw": load_animation_images("Throw"),
                          "Dead": load_animation_images("Dead")}}
