import pygame, sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
fps_clock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("lokavapour")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

p1_x = 10
p1_y = 300
p2_x = 790
p2_y = 300
ball_x = 400
ball_y = 300

p1_points = 0
p2_points = 0

#ball_direction tölur: 0 = left; 1 = right; 2 = start; 3 = left up; 4 = left down; 5 = right up; 6 = right down
p1_direction = "STOP"
p2_direction = "STOP"
ball_direction = 2

def score(p1_points, p2_points):
    window_width = 800
    basic_font = pygame.font.Font("freesansbold.ttf", 18)
    p1_score_surf = basic_font.render("%s" % (p1_points), True, WHITE)
    p2_score_surf = basic_font.render("%s" % (p2_points), True, WHITE)
    p1_score_rect = p1_score_surf.get_rect()
    p2_score_rect = p2_score_surf.get_rect()
    p1_score_rect.topleft = (window_width - 500, 10)
    p2_score_rect.topleft = (window_width - 300, 10)
    DISPLAYSURF.blit(p1_score_surf, p1_score_rect)
    DISPLAYSURF.blit(p2_score_surf, p2_score_rect)

while True:
    DISPLAYSURF.fill(BLACK)
    score(p1_points, p2_points)
    ball = pygame.draw.rect(DISPLAYSURF, WHITE, (ball_x, ball_y, 10, 10))
    player1 = pygame.draw.line(DISPLAYSURF, WHITE, (p1_x, p1_y - 50), (p1_x, p1_y + 50), 10)
    player2 = pygame.draw.line(DISPLAYSURF, WHITE, (p2_x, p2_y - 50), (p2_x, p2_y + 50), 10)
    if p1_direction == "UP":
        p1_y -= 10
    elif p1_direction == "DOWN":
        p1_y += 10
    elif p1_direction == "STOP":
        p1_y = p1_y
    if p2_direction == "UP":
        p2_y -= 10
    elif p2_direction == "DOWN":
        p2_y += 10
    elif p2_direction == "STOP":
        p2_y = p2_y
    if ball_direction == 2: #random átt
        ball_direction = random.randrange(0, 2)
    elif ball_direction == 0: #vinstri
        ball_x -= 5
    elif ball_direction == 1: #hægri
        ball_x += 5
    elif ball_direction == 3: #vinstri upp
        ball_x -= 5
        ball_y -= 1
        if ball_y == 0: #ef kúlan hittir toppinn á glugganum skoppar hún niður
            ball_direction = 4
    elif ball_direction == 4: #vinstri niður
        ball_x -= 5
        ball_y += 1
        if ball_y == 590: #ef kúlan hittir botnin á glugganum skoppar hún upp
            ball_direction = 3
    elif ball_direction == 5: #hægri upp
        ball_x += 5
        ball_y -= 1
        if ball_y == 0: #sama fyrir hægri
            ball_direction = 6
    elif ball_direction == 6: #hægri niður
        ball_x += 5
        ball_y += 1
        if ball_y == 590: #sama fyrir hægri
            ball_direction = 5

    if ball_x == p1_x and ball_y == p1_y: #ef kúlan hittir miðjuna á player 1 þá skýst hún beint áfram til hægri
        ball_direction = 1
    elif ball_x == p1_x and ball_y >= p1_y - 50 and ball_y <= p1_y: #ef kúlan hittir efri hlutan á player 1 þá skýst hún upp og til hægri
        ball_direction = 5
    elif ball_x == p1_x and ball_y <= p1_y + 50 and ball_y >= p1_y: #ef kúlan hittir neðri hlutan á player 1 þá skýst hún niður og til hægri
        ball_direction = 6
    #sama fyrir player 2
    if ball_x == p2_x and ball_y == p2_x:
        ball_direction = 0
    elif ball_x == p2_x and ball_y >= p2_y - 50 and ball_y <= p1_y:
        ball_direction = 3
    elif ball_x == p2_x and ball_y <= p2_y + 50 and ball_y >= p1_y:
        ball_direction = 4

    #skora
    if ball_x == 0:
        ball_x = 400
        ball_y = 300
        p1_y = 300
        p2_y = 300
        ball_direction = 2
        p2_points += 1
    elif ball_x == 800:
        ball_x = 400
        ball_y = 300
        p1_y = 300
        p2_y = 300
        ball_direction = 2
        p1_points += 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_UP):
                p2_direction = "UP"
            elif (event.key == K_DOWN):
                p2_direction = "DOWN"
            elif (event.key == K_w):
                p1_direction = "UP"
            elif (event.key == K_s):
                p1_direction = "DOWN"
        elif event.type == KEYUP:
            if (event.key == K_UP):
                p2_direction = "STOP"
            elif (event.key == K_DOWN):
                p2_direction = "STOP"
            elif (event.key == K_w):
                p1_direction = "STOP"
            elif (event.key == K_s):
                p1_direction = "STOP"
    
    pygame.display.update()
    fps_clock.tick(FPS)
