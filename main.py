import os
import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

os.environ['SDL_VIDEO_CENTERED'] = '1'

RES = WIDTH, HEIGHT = (800,800)
FPS = 60

pixel_width = 200
pixel_height = 200
x_pixel = 0
y_pixel = 0

screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height 

screen_size = screen_width * screen_height

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption('3D Donut')
font = pygame.font.SysFont('Arial',50,bold=True)

def text_display(char,x,y):
    text = font.render(str(char),True,WHITE)
    text_rect = text.get_rect(center=(x,y))
    screen.blit(text,text_rect)

k=0
running = True
while running:
  clock.tick(FPS)
  screen.fill(BLACK)

  output = ['+'] * screen_size

  for i in range(screen_height):
    y_pixel += pixel_height
    for j in range(screen_width):
      x_pixel += pixel_width
      text_display(output[k],x_pixel - pixel_width//2,y_pixel - pixel_height//2)
      k+=1
    x_pixel=0
  y_pixel=0
  k=0

  pygame.display.update()

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              running = False