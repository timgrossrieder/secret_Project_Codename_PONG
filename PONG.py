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

    def __init__(self, x, y, x_speed, y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def zeichne_Spielball(self):
        pygame.draw.circle(DISPLAYSURF, GAME_COLOUR, (int(self.x), int(self.y)), 10)

    def Ballbewegung(self):
        self.x = (self.x + self.x_speed)
        if (self.y + 10) < (BOARD_HEIGHT/10*9) and (self.y - 10) > (BOARD_HEIGHT/10 + 10):
            self.y = (self.y + self.y_speed)
        else:
            self.y_speed = self.y_speed * -1
            self.y = (self.y + self.y_speed)


#Ballspeed
ball_speed_x = -0.1
ball_speed_y = 0.3

# Ballpositionen
xBall = int(BOARD_LENGTH / 2)
yBall = int(BOARD_HEIGHT / 2) + 5

# Schläger
# Starthöhen Schläger
Hoehe_S1 = BOARD_HEIGHT / 2
Hoehe_S2 = BOARD_HEIGHT / 2

Schlaegerspeed = 0.5

class Schlaeger():
    def __init__(self, x, y, Schlaegerspeed):
        self.x = x
        self.y = y
        self.speed = Schlaegerspeed

    def zeichne_Schlaeger(self):
        pygame.draw.rect(DISPLAYSURF, GAME_COLOUR,(self.x, self.y, BOARD_LENGTH/50, BOARD_HEIGHT/5))

    def Schlaegerbewegung(self):
        keys = pygame.key.get_pressed()
        if self == S1:
            if keys[K_s] and (self.y + self.speed) <= (BOARD_HEIGHT/10*9 - BOARD_HEIGHT/5):
                self.y = self.y + self.speed
            if keys[K_w] and (self.y - self.speed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - self.speed
        elif self == S2:
            if keys[K_l] and (self.y + self.speed) <= (BOARD_HEIGHT/10*9 - BOARD_HEIGHT/5):
                self.y = self.y + self.speed
            if keys[K_o] and (self.y - self.speed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - self.speed
        return self.y


S1 = Schlaeger(BOARD_LENGTH / 10, Hoehe_S1, Schlaegerspeed)
S2 = Schlaeger(BOARD_LENGTH / 10 * 9 - BOARD_LENGTH / 50, Hoehe_S2, Schlaegerspeed)
Ball = Spielball(xBall,yBall, ball_speed_x, ball_speed_y)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    Spielfeld()
    Hoehe_S1 = S1.Schlaegerbewegung()
    Hoehe_S2 = S2.Schlaegerbewegung()
    S1.zeichne_Schlaeger()
    S2.zeichne_Schlaeger()
    Ball.Ballbewegung()
    xBall = Ball.x
    yBall = Ball.y
    Ball.zeichne_Spielball()


    pygame.display.update()