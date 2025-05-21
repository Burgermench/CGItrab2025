import pygame
from engine.scene import GameScene

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("CG Hero: play 'em all")
    
clock = pygame.time.Clock()

scene = GameScene(screen)

running = True
while running:
    dt = clock.tick(60) / 1000          # Delta time in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene.update(dt)
    scene.render()

    pygame.display.flip()

pygame.quit()