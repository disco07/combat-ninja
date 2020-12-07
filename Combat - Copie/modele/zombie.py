import pygame
import random


class Zombie(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 0.1
        self.health = 100
        self.max_health = 100
        self.velocity = random.random()
        self.image = pygame.image.load("./assets/Idle (1).png")
        self.image = pygame.transform.scale(self.image, (100, 180))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 990 + random.randint(0, 500)
        self.rect.y = 505

    def damage(self, point_attack):
        self.health -= point_attack
        if self.health <= 0:
            # faire reapparaitre le zombie de nouveau
            self.rect.x = 990 + random.randint(0, 300)
            self.velocity = random.random()
            self.health = self.max_health

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x, self.rect.y, self.health, 5]
        back_bar_position = [self.rect.x, self.rect.y, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def move_zombie(self):
        if not self.game.check_collision(self, self.game.player_group):
            self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.player_group):
            self.game.player.damage(self.attack)
