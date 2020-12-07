import pygame


class Kunai(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.attack = 20
        self.velocity = 2
        self.image = pygame.image.load(f"./assets/ninja/Kunai.png")
        self.image = pygame.transform.scale(self.image, (50, 15))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 60
        self.rect.y = player.rect.y + 70

    def remove(self):
        self.player.kunai_group.remove(self)

    def move_kunai(self):
        self.rect.x += self.velocity
        for zombie in self.player.game.check_collision(self, self.player.game.zombie_group):
            zombie.damage(self.attack)
            self.remove()

        if self.rect.x > 1080:
            self.remove()

