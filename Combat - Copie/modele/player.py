import modele.animation
from  modele.kunai import Kunai
import pygame


class Player(modele.animation.AnimateSprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 30
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 530
        self.is_jumping = False
        self.jump = 5
        self.kunai_group = pygame.sprite.Group()
        self.launch = False

    def damage(self, point_attack):
        if self.health - point_attack > point_attack:
            self.health -= point_attack
        if self.health <= 0.11:
            self.animation("Dead", "Right")

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x - 10, self.rect.y - 10, self.health, 5]
        back_bar_position = [self.rect.x - 10, self.rect.y - 10, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_kunai(self):
        self.kunai_group.add(Kunai(self))

    def throw_kunai(self):
        self.start_animation()
        self.animation("Throw", "right")

    def move_right(self):
        self.start_animation()
        self.animation("Run", "right")
        if not self.game.check_collision(self, self.game.zombie_group):
            self.rect.x += self.velocity

    def move_left(self):
        self.start_animation()
        self.rect.x -= self.velocity
        self.animation("Run", "left")

    def stand_animation(self, direction):
        self.start_animation()
        self.animation("Idle", direction)

    def move_down(self, direction):
        self.animation("Slide", direction)

    def move_up(self, direction):
        self.start_animation()
        self.animation("Jump", direction)
