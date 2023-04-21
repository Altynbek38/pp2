import pygame
import math
pygame.init()

W, H = 800, 800

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
sc.fill(WHITE)

clock = pygame.time.Clock()
FPS = 60

class Button:
    def __init__(self):
        self.rect_pen = pygame.Rect(10, 10, 50, 50)
        self.rect_rect = pygame.Rect(65, 10, 50, 50)
        self.rect_circle = pygame.Rect(120, 10, 50, 50)
        self.rect_eraser = pygame.Rect(175, 10, 50, 50)
        self.rect_red = pygame.Rect(750, 10, 40, 40)
        self.rect_green = pygame.Rect(695, 10, 40, 40)
        self.rect_blue = pygame.Rect(640, 10, 40, 40)
        self.rect_black = pygame.Rect(585, 10, 40, 40)
        self.image_pen = pygame.image.load(r'C:\pp2\week11\paint\images\pen.png')
        self.image_circle = pygame.image.load(r'C:\pp2\week11\paint\images\circle.png')
        self.image_eraser = pygame.image.load(r'C:\pp2\week11\paint\images\eraser.png')
    
    def draw(self):
        self.pen = sc.blit(self.image_pen, self.rect_pen)
        self.rect = pygame.draw.rect(sc, BLACK, self.rect_rect, 1)
        self.red = pygame.draw.rect(sc, RED, self.rect_red)
        self.green = pygame.draw.rect(sc, GREEN, self.rect_green)
        self.blue = pygame.draw.rect(sc, BLUE, self.rect_blue)
        self.black = pygame.draw.rect(sc, BLACK, self.rect_black)
        self.circle = sc.blit(self.image_circle, self.rect_circle)
        self.eraser = sc.blit(self.image_eraser, self.rect_eraser)
    
class Pen:
    def __init__(self, pos, colour):
        self.line = []
        self.line.append(pos)
        self.start_pos = pos
        self.colour = colour
    
    def draw(self):
        for x in range(len(self.line) - 1):
            pygame.draw.line(sc, self.colour, self.line[x], self.line[x+1], 5)
    
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.line.append(current_pos)
        for obj in drawings:
            obj.draw()

    
class Eraser:
    def __init__(self, pos):
        self.line = []
        self.line.append(pos)
        self.start_pos = pos
        self.colour = WHITE
    
    def draw(self):
        for x in range(len(self.line) - 1):
            pygame.draw.line(sc, self.colour, self.line[x], self.line[x+1], 5)
    
    def update(self, current_pos, drawings):
        self.line.append(current_pos)
        for obj in drawings:
            obj.draw()

class Rect:
    def __init__(self, pos, colour):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
    
    def draw(self):
        self.width =  abs(self.end_pos[0] - self.start_pos[0])
        self.height =  abs(self.end_pos[1] - self.start_pos[1])
        pygame.draw.rect(sc, self.colour, pygame.Rect(min(self.end_pos[0], self.start_pos[0]), min(self.end_pos[1], self.start_pos[1]), self.width, self.height), 1)

    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

class Circle:
    def __init__(self, pos, colour):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
    
    def draw(self):
        radius = int(math.sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2))
        pygame.draw.circle(sc, self.colour, (self.start_pos[0], self.start_pos[1]), radius, 1)
    
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

button = Button()
shape = 'pen'
colour = BLACK
drawings = []
objects = None
flStartDrawing = False
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.pen.collidepoint(pygame.mouse.get_pos()): shape = 'pen'
            elif button.rect.collidepoint(pygame.mouse.get_pos()): shape = 'rect'
            elif button.circle.collidepoint(pygame.mouse.get_pos()): shape = 'circle'
            elif button.eraser.collidepoint(pygame.mouse.get_pos()): shape = 'eraser'

            if button.red.collidepoint(pygame.mouse.get_pos()): colour = RED
            elif button.green.collidepoint(pygame.mouse.get_pos()): colour = GREEN
            elif button.blue.collidepoint(pygame.mouse.get_pos()): colour = BLUE
            elif button.black.collidepoint(pygame.mouse.get_pos()): colour = BLACK

            if shape == 'pen':
                object = Pen(pygame.mouse.get_pos(), colour)
                flStartDrawing = True
            elif shape == 'rect': 
                object = Rect(pygame.mouse.get_pos(), colour)
                flStartDrawing = True
            elif shape == 'circle':
                object = Circle(pygame.mouse.get_pos(), colour)
                flStartDrawing = True
            elif shape == 'eraser':
                object = Eraser(pygame.mouse.get_pos())
                flStartDrawing = True
        if event.type == pygame.MOUSEMOTION and flStartDrawing:
            object.update(pygame.mouse.get_pos(), drawings)
            object.draw()
        if event.type == pygame.MOUSEBUTTONUP and shape != 'eraser':
            drawings.append(object)
            object = None
            flStartDrawing = False
        elif event.type == pygame.MOUSEBUTTONUP and shape == 'eraser':
            pen = []
            drawings.append(object)
            object = None
            flStartDrawing = False

    button.draw()
    pygame.display.update()

pygame.quit()