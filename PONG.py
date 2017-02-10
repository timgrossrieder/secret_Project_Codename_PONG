import pygame, sys
from pygame.locals import *
#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (188, 188, 188)
DARKGREY = (40, 40, 40)

BOARD_LENGTH = 1000
BOARD_HEIGHT = 600
GAME_COLOUR = BLACK

pygame.init()

DISPLAYSURF = pygame.display.set_mode((BOARD_LENGTH, BOARD_HEIGHT))
pygame.display.set_caption('PONG123')

#Spielfeld
DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, GAME_COLOUR, ((BOARD_LENGTH/10), (BOARD_HEIGHT/10), (BOARD_LENGTH*0.8), 10))
pygame.draw.rect(DISPLAYSURF, GAME_COLOUR, ((BOARD_LENGTH/10), (BOARD_HEIGHT/10*9), (BOARD_LENGTH*0.8), 10))
def make_mid_line(y):
    pygame.draw.rect(DISPLAYSURF, GREY, (BOARD_LENGTH/2-5, y, 10, BOARD_HEIGHT/20))
for n in range (1, 9):
    make_mid_line(n*BOARD_HEIGHT/10+20)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()