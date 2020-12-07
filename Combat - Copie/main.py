from modele.game import Game
import pygame

pygame.init()

pygame.display.set_caption('Ninja game')
screen = pygame.display.set_mode((1080, 720))
bg_image = pygame.image.load("./assets/bg.jpg")

running = True
game = Game()
clock = pygame.time.Clock()

while running:

    clock.tick(120)

    # charger le background sur le screen
    screen.blit(bg_image, (0, -200))

    game.update(screen)

    # mettre a jour le screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter si un joueur appuie une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed_down[event.key] = True
            game.pressed_up[event.key] = False
            game.key_up[0] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_kunai()

        elif event.type == pygame.KEYUP:
            game.pressed_up[event.key] = True
            game.pressed_down[event.key] = False
            game.key[0] = event.key
            game.key_up[0] = False
