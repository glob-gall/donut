import os
import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

os.environ['SDL_VIDEO_CENTERED'] = '1'

RES = WHITE, HEIGHT = (800,800)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption('3D Donut')


running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False