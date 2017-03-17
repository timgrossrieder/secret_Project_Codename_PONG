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
pygame.display.set_caption('PONG')

#Spielfeld
def Spielfeld():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, GAME_COLOUR, ((BOARD_LENGTH/10), (BOARD_HEIGHT/10), (BOARD_LENGTH*0.8), 10))
    pygame.draw.rect(DISPLAYSURF, GAME_COLOUR, ((BOARD_LENGTH/10), (BOARD_HEIGHT/10*9), (BOARD_LENGTH*0.8), 10))
    def make_mid_line(y):
        pygame.draw.rect(DISPLAYSURF, GREY, (BOARD_LENGTH/2-5, y, 10, BOARD_HEIGHT/20))
    for n in range (1, 9):
        make_mid_line(n*BOARD_HEIGHT/10+(BOARD_LENGTH/50))

# Spielball
class Spielball:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def zeichne_Spielball(self):
        pygame.draw.circle(DISPLAYSURF, GAME_COLOUR, (self.x, self.y), 10)

# Ballpositionen
xBall = int(BOARD_LENGTH / 2)
yBall = int(BOARD_HEIGHT / 2) + 5

# Schläger
# Starthöhen Schläger
Hoehe_S1 = BOARD_HEIGHT / 2
Hoehe_S2 = BOARD_HEIGHT / 2

Schlaegerspeed = 0.5

class Schlaeger():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def zeichne_Schlaeger(self):
        pygame.draw.rect(DISPLAYSURF, GAME_COLOUR,(self.x, self.y, BOARD_LENGTH/50, BOARD_HEIGHT/5))

    def Schlaegerbewegung(self, Schlaegerspeed):
        keys = pygame.key.get_pressed()
        if self == S1:
            if keys[K_s] and (self.y + Schlaegerspeed) <= (BOARD_HEIGHT/10*9 - BOARD_HEIGHT/5):
                self.y = self.y + Schlaegerspeed
            if keys[K_w] and (self.y - Schlaegerspeed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - Schlaegerspeed
        elif self == S2:
            if keys[K_l] and (self.y + Schlaegerspeed) <= (BOARD_HEIGHT/10*9 - BOARD_HEIGHT/5):
                self.y = self.y + Schlaegerspeed
            if keys[K_o] and (self.y - Schlaegerspeed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - Schlaegerspeed
        return self.y

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    Spielfeld()
    S1 = Schlaeger(BOARD_LENGTH/10, Hoehe_S1)
    S2 = Schlaeger(BOARD_LENGTH/10*9-BOARD_LENGTH/50, Hoehe_S2)
    Hoehe_S1 = S1.Schlaegerbewegung(Schlaegerspeed)
    Hoehe_S2 = S2.Schlaegerbewegung(Schlaegerspeed)
    S1.zeichne_Schlaeger()
    S2.zeichne_Schlaeger()
    Ball = Spielball(xBall,yBall)
    Ball.zeichne_Spielball()

    pygame.display.update()