import pygame, sys
import random
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

# Balleigenschaften
Radius = 10

# Ballspeed
ball_speed_x = 0.5
ball_speed_y = 0
ball_speed_y_max = 2

# Ballpositionen
xBall = int(BOARD_LENGTH / 2)
yBall = int(BOARD_HEIGHT / 2) + 5

def check_Schlaegerkollision():
    if Ball.x + Ball.radius > ((BOARD_LENGTH / 10 * 9) - 20) and (Ball.y + Ball.radius > S2.y and Ball.y - Ball.radius < S2.y + S2.laenge):
        Ball.x_speed = -abs(Ball.x_speed)
        if  abs(Ball.y_speed - ((S2.y + S2.laenge / 2) - Ball.y) / 1000) < Ball.y_speed_max:
            Ball.y_speed = Ball.y_speed - ((S2.y + S2.laenge / 2) - Ball.y) / 100
        else:
            if Ball.y_speed == abs(Ball.y_speed):
                Ball.y_speed = Ball.y_speed_max
            else:
                Ball.y_speed = -Ball.y_speed_max


    if Ball.x - Ball.radius < ((BOARD_LENGTH / 10) + 20) and (Ball.y + Ball.radius > S1.y and Ball.y - Ball.radius < S1.y + S1.laenge):
        Ball.x_speed = abs(Ball.x_speed)
        if abs(Ball.y_speed - ((S1.y + S1.laenge / 2) - Ball.y) / 1000) < Ball.y_speed_max:
            Ball.y_speed = Ball.y_speed - ((S1.y + S1.laenge / 2) - Ball.y) / 100
        else:
            if Ball.y_speed == abs(Ball.y_speed):
                Ball.y_speed = Ball.y_speed_max
            else:
                Ball.y_speed = -Ball.y_speed_max


# Spielball
class Spielball:

    def __init__(self, x, y, x_speed, y_speed, y_speed_max, radius):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.y_speed_max = y_speed_max
        self.radius = radius

    def zeichne_Spielball(self):
        pygame.draw.circle(DISPLAYSURF, GAME_COLOUR, (int(self.x), int(self.y)), self.radius)

    def Ballbewegung(self):
        check_Schlaegerkollision()
        self.x = (self.x + self.x_speed)
        if (self.y + 10) < (BOARD_HEIGHT/10*9) and (self.y - 10) > (BOARD_HEIGHT/10 + 10):
            self.y = (self.y + self.y_speed)
        else:
            self.y_speed = self.y_speed * -1
            self.y = (self.y + self.y_speed)
        self.x_speed = self.x_speed * 1.00005


# Schläger
# Starthöhen Schläger
Hoehe_S1 = BOARD_HEIGHT / 2
Hoehe_S2 = BOARD_HEIGHT / 2

Schlaegerspeed = 0.7

class Schlaeger():
    def __init__(self, x, y, Schlaegerspeed):
        self.x = x
        self.y = y
        self.speed = Schlaegerspeed
        self.laenge = BOARD_HEIGHT/5
        self.dicke = BOARD_LENGTH/50

    def zeichne_Schlaeger(self):
        pygame.draw.rect(DISPLAYSURF, GAME_COLOUR,(self.x, self.y, BOARD_LENGTH/50, self.laenge))

    def Schlaegerbewegung(self):
        keys = pygame.key.get_pressed()
        if self == S1 and status == "PvP":
            if keys[K_s] and (self.y + self.speed) <= (BOARD_HEIGHT/10*9 - self.laenge):
                self.y = self.y + self.speed
            if keys[K_w] and (self.y - self.speed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - self.speed
        elif self == S2:
            if keys[K_l] and (self.y + self.speed) <= (BOARD_HEIGHT/10*9 - self.laenge):
                self.y = self.y + self.speed
            if keys[K_o] and (self.y - self.speed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - self.speed

        elif status == "Easy" or status == "Hard" or status == "Destroyer":
            if status == "Easy":
                schwierigkeit = 0.5
            if status == "Hard":
                schwierigkeit = 0.8
            if status == "Destroyer":
                schwierigkeit = 1
            if Ball.y < self.y + self.laenge / 2 and random.random() < schwierigkeit and (self.y + self.speed) >= (BOARD_HEIGHT/10 + 10):
                self.y = self.y - self.speed
            if Ball.y > self.y + self.laenge / 2 and random.random() < schwierigkeit and (self.y - self.speed) <= (BOARD_HEIGHT/10*9 - self.laenge):
                self.y = self.y + self.speed


Resultat = [0, 0]

def Spielstand():
    if Ball.x - Ball.radius < (BOARD_LENGTH / 10):
        Resultat[1] = Resultat[1] + 1
        Ball.x = xBall
        Ball.y = yBall
        Ball.y_speed = ball_speed_y
        Ball.x_speed = -ball_speed_x
    if Ball.x + Ball.radius > (BOARD_LENGTH / 10 * 9):
        Resultat[0] = Resultat[0] + 1
        Ball.x = xBall
        Ball.y = yBall
        Ball.y_speed = ball_speed_y
        Ball.x_speed = ball_speed_x

def Anzeige():
    font = pygame.font.SysFont("comicsansms", 72)
    text = font.render((str(Resultat[0])+" : "+ str(Resultat[1])), True, (BLACK))
    DISPLAYSURF.blit(text, (BOARD_LENGTH / 2 - text.get_width() // 2, BOARD_HEIGHT / 50))

    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render(("ENTER drücken um das Spiel zu beenden"), True, (BLACK))
    DISPLAYSURF.blit(text, (BOARD_LENGTH / 2 - text.get_width() // 2, BOARD_HEIGHT / 50 * 49 - text.get_height()))

S1 = Schlaeger(BOARD_LENGTH / 10, Hoehe_S1, Schlaegerspeed)
S2 = Schlaeger(BOARD_LENGTH / 10 * 9 - BOARD_LENGTH / 50, Hoehe_S2, Schlaegerspeed)
Ball = Spielball(xBall, yBall, ball_speed_x, ball_speed_y, ball_speed_y_max, Radius)

FPS = 2000
FPSCLOCK = pygame.time.Clock()

def easteregg():
    if Resultat[0] == Resultat[1] == 8:
        font = pygame.font.SysFont("comicsansms", 80)
        text = font.render(("Haha"), True, (RED))
        DISPLAYSURF.blit(text, (BOARD_LENGTH / 2 - text.get_width() // 2, BOARD_HEIGHT / 2 - text.get_height() // 2))
        pygame.display.update()

def button(x, y, laenge, hoehe, farbe, name, textgroesse):
    pygame.draw.rect(DISPLAYSURF, farbe, (x, y, laenge, hoehe))
    font = pygame.font.SysFont("comicsansms", textgroesse)
    text = font.render((name), True, (BLACK))
    DISPLAYSURF.blit(text, (x + (laenge - text.get_width()) / 2, y + (hoehe - text.get_height()) / 2))
    mouse = pygame.mouse.get_pos()
    if x < mouse[0] < x + laenge and y < mouse[1] < y + hoehe:
        return True
    else:
        return False


# main game loop
status = "Start"
while status == "Start":
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)
    font = pygame.font.SysFont("comicsansms", 72)
    text = font.render(("Choose your Mode"), True, (WHITE))
    DISPLAYSURF.blit(text, (BOARD_LENGTH / 2 - text.get_width() // 2, BOARD_HEIGHT / 6))

    if button(BOARD_LENGTH/2 - 250, BOARD_HEIGHT/2 - 100, 200, 50, WHITE, "PvP", 50):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = "PvP"

    if button(BOARD_LENGTH/2 + 50, BOARD_HEIGHT/2 - 100, 200, 50, WHITE, "Easy", 50):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = "Easy"

    if button(BOARD_LENGTH/2 - 250, BOARD_HEIGHT/2 + 50, 200, 50, WHITE, "Hard", 50):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = "Hard"

    if button(BOARD_LENGTH/2 + 50, BOARD_HEIGHT/2 + 50, 200, 50, WHITE, "Destroyer", 50):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = "Destroyer"

    pygame.display.update()


while status == "PvP" or status == "Easy" or status == "Hard" or status == "Destroyer":
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            status == "Ende"
    Spielfeld()
    S1.Schlaegerbewegung()
    S2.Schlaegerbewegung()
    S1.zeichne_Schlaeger()
    S2.zeichne_Schlaeger()
    Ball.Ballbewegung()
    Ball.zeichne_Spielball()
    Spielstand()
    Anzeige()
    easteregg()

    pygame.display.update()
    FPSCLOCK.tick(FPS)


while status == "Ende":
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)

    font = pygame.font.SysFont("comicsansms", 72)

    if Resultat[0] < Resultat[1]:
        text = font.render(("Der rechte Spieler hat gewonnen!"), True, (WHITE))

    if Resultat[0] > Resultat[1]:
        text = font.render(("Der linke Spieler hat gewonnen!"), True, (WHITE))

    if Resultat[0] == Resultat[1]:
        text = font.render(("Unentschieden!"), True, (WHITE))

    DISPLAYSURF.blit(text, (BOARD_LENGTH / 2 - text.get_width() // 2, BOARD_HEIGHT / 2 - text.get_height() // 2))

    pygame.display.update()