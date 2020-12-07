from modele.player import Player
from modele.zombie import Zombie
import pygame


class Game(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # creation du joueur
        self.player_group = pygame.sprite.Group()
        self.player = Player(self)
        self.player_group.add(self.player)
        # creation du zombie
        self.zombie_group = pygame.sprite.Group()
        self.pressed_down = {}
        self.pressed_up = {}
        self.key = [0]
        self.key_up = [0]
        self.count = 0
        self.spawn_zombie()
        self.spawn_zombie()

    def spawn_zombie(self):
        self.zombie_group.add(Zombie(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self, screen):
        for kunai in self.player.kunai_group:
            kunai.move_kunai()

        for zombie in self.zombie_group:
            zombie.move_zombie()
            zombie.update_health_bar(screen)
        # charger le joueur
        self.player.update_health_bar(screen)

        screen.blit(self.player.image, self.player.rect)
        self.player.kunai_group.draw(screen)
        self.zombie_group.draw(screen)
        # verifier la touche appuyée
        if self.pressed_down.get(pygame.K_SPACE):
            self.player.throw_kunai()
        elif self.pressed_down.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed_down.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.key_up:
            if self.key[0] == 1073741904:
                self.player.stand_animation('left')
            elif self.key[0] == 1073741903:
                self.player.stand_animation('right')

        if not self.player.is_jumping:
            if self.pressed_down.get(pygame.K_UP):
                self.player.is_jumping = True
        else:
            if self.player.jump >= -5:
                self.player.rect.y -= (self.player.jump * abs(self.player.jump))
                self.player.move_up('left')
                self.player.jump -= 1
            else:
                self.player.jump = 5
                self.player.is_jumping = False
                self.player.stand_animation('right')
