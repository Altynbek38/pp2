import pygame
import math
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

W, H = 800, 800
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
sc.fill(WHITE)

clock = pygame.time.Clock()
FPS = 60

DRAW = ''
COLOUR = BLACK

image_eraser = pygame.image.load(r'C:\pp2\week11\paint\eraser.png')
image_circle = pygame.image.load(r'C:\pp2\week11\paint\circle.png')

rect_rect = pygame.Rect(10, 10, 50, 50)
rect_circle = pygame.Rect(65, 10, 50, 50)
rect_eraser = pygame.Rect(120, 10, 50, 50)
rect_red = pygame.Rect(750, 10, 40, 40)
rect_green = pygame.Rect(695, 10, 40, 40)
rect_blue = pygame.Rect(640, 10, 40, 40)
rect_black = pygame.Rect(585, 10, 40, 40)

sp = ep = None

def draw_rect(sp, pos):
    pygame.draw.rect(sc, COLOUR, pygame.Rect(min(pos[0], sp[0]), min(pos[1], sp[1]), abs(pos[0] - sp[0]), abs(pos[1] - sp[1])), 1)

def draw_circle(sp, pos):
    radius = int(math.sqrt((pos[0] - sp[0])**2 + (pos[1] - sp[1])**2))
    pygame.draw.circle(sc, COLOUR, sp, radius, 2)

flRunning = True
flStartDraw = False
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                DRAW = 'Rect'
            elif event.key == pygame.K_2:
                DRAW = 'Circle'
            if event.key == pygame.K_r:
                COLOUR = RED
            elif event.key == pygame.K_g:
                COLOUR = GREEN
            elif event.key == pygame.K_b:
                COLOUR = BLUE
            elif event.key == pygame.K_v:
                COLOUR = BLACK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flStartDraw = True
            sp = pygame.mouse.get_pos()
        # elif event.type == pygame.MOUSEMOTION:
        #     if flStartDraw:
        #         pos = pygame.mouse.get_pos()
        #         draw_rect(sp, pos)
        #         pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if DRAW == 'Rect':
                draw_rect(sp, pos)
            elif DRAW == 'Circle':
                draw_circle(sp, pos)
               
    pygame.draw.rect(sc, RED, rect_red)
    pygame.draw.rect(sc, GREEN, rect_green)
    pygame.draw.rect(sc, BLUE, rect_blue)
    pygame.draw.rect(sc, BLACK, rect_black)
    pygame.draw.rect(sc, BLACK, rect_rect, 1)
    sc.blit(image_eraser, rect_eraser)
    sc.blit(image_circle, rect_circle)
    # sc.blit(drawing_surface, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()