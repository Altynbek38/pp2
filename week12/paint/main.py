#Imports and initializing
import pygame
import math
pygame.init()

#Colours
W, H = 800, 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)
PINK = (255, 0, 255)
GREY = (192, 192, 192)

#Display settings
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
sc.fill(WHITE)

#Tick Rate
clock = pygame.time.Clock()
FPS = 60

#Class to create a interface with buttons no the screen
class Button:
    def __init__(self):
        self.rect_pen = pygame.Rect(10, 10, 50, 50)
        self.rect_square = pygame.Rect(65, 10, 50, 50)
        self.rect_rect = pygame.Rect(120, 15, 50, 40)
        self.rect_circle = pygame.Rect(175, 10, 50, 50)
        self.rect_eraser = pygame.Rect(230, 10, 50, 50)
        self.rect_right_triangle = pygame.Rect(285, 10, 50, 50)
        self.rect_equilateral_triangle = pygame.Rect(340, 10, 50, 50)
        self.rect_rhombus = pygame.Rect(395, 10, 50, 50)
        self.rect_size_reduce = pygame.Rect(450, 10, 50, 50)
        self.rect_size_rise = pygame.Rect(505, 10, 50, 50)
        self.rect_red = pygame.Rect(750, 10, 40, 40)
        self.rect_green = pygame.Rect(695, 10, 40, 40)
        self.rect_blue = pygame.Rect(640, 10, 40, 40)
        self.rect_black = pygame.Rect(585, 10, 40, 40)
        self.rect_yellow = pygame.Rect(640, 50, 40, 40)
        self.rect_orange = pygame.Rect(750, 50, 40, 40)
        self.rect_pink = pygame.Rect(695, 50, 40, 40)
        self.rect_grey = pygame.Rect(585, 50, 40, 40)
        self.image_pen = pygame.image.load(r'C:\pp2\week12\paint\images\pen.png')
        self.image_circle = pygame.image.load(r'C:\pp2\week12\paint\images\circle.png')
        self.image_eraser = pygame.image.load(r'C:\pp2\week12\paint\images\eraser.png')
        self.image_right_triangle = pygame.image.load(r'C:\pp2\week12\paint\images\right_triangle.png')
        self.image_equilateral_triangle = pygame.image.load(r'C:\pp2\week12\paint\images\equilateral_triangle.png')
        self.image_rhombus = pygame.image.load(r'C:\pp2\week12\paint\images\rhombus.png')
        self.image_size_reduce = pygame.image.load(r'C:\pp2\week12\paint\images\size_reduce.png')
        self.image_size_rise = pygame.image.load(r'C:\pp2\week12\paint\images\size_rise.png')       

    def draw(self):
        self.pen = sc.blit(self.image_pen, self.rect_pen)
        self.square = pygame.draw.rect(sc, BLACK, self.rect_square, 1)
        self.rect = pygame.draw.rect(sc, BLACK, self.rect_rect, 1)
        self.red = pygame.draw.rect(sc, RED, self.rect_red)
        self.green = pygame.draw.rect(sc, GREEN, self.rect_green)
        self.blue = pygame.draw.rect(sc, BLUE, self.rect_blue)
        self.black = pygame.draw.rect(sc, BLACK, self.rect_black)
        self.yellow = pygame.draw.rect(sc, YELLOW, self.rect_yellow)
        self.orange = pygame.draw.rect(sc, ORANGE, self.rect_orange)
        self.pink = pygame.draw.rect(sc, PINK, self.rect_pink)
        self.grey = pygame.draw.rect(sc, GREY, self.rect_grey)
        self.circle = sc.blit(self.image_circle, self.rect_circle)
        self.eraser = sc.blit(self.image_eraser, self.rect_eraser)
        self.right_triangle = sc.blit(self.image_right_triangle, self.rect_right_triangle)
        self.equilateral_triangle = sc.blit(self.image_equilateral_triangle, self.rect_equilateral_triangle)
        self.rhombus = sc.blit(self.image_rhombus, self.rect_rhombus)
        self.size_reduce = sc.blit(self.image_size_reduce, self.rect_size_reduce)
        self.size_rise = sc.blit(self.image_size_rise, self.rect_size_rise)

#Class to draw with a pen, also to erase
class Pen:
#Initialize class settings and gets positions of some amount of lines in every second, Pen tool draws with large amount of broken lines and seems like you are drawing with Pen 
    def __init__(self, pos, colour, size):
        self.line = []
        self.line.append(pos)
        self.start_pos = pos
        self.colour = colour
        self.size = size

#loop iterates line positions and draws on the screen
    def draw(self):
        for x in range(len(self.line) - 1):
            pygame.draw.line(sc, self.colour, self.line[x], self.line[x+1], self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.line.append(current_pos)
        for object in drawings:
            object.draw()
    
#Class to draw a rectangle
class Rect:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds the width, height, and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        self.width =  abs(self.end_pos[0] - self.start_pos[0])
        self.height =  abs(self.end_pos[1] - self.start_pos[1])
        pygame.draw.rect(sc, self.colour, pygame.Rect(min(self.end_pos[0], self.start_pos[0]), min(self.end_pos[1], self.start_pos[1]), self.width, self.height), self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

#Class to draw a square
class Square:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds the width, height, and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        self.width = abs(self.end_pos[0] - self.start_pos[0])
        self.height = abs(self.end_pos[1] - self.start_pos[1])
        side_length = max(self.width, self.height)
        if self.start_pos[0] < self.end_pos[0] and self.start_pos[1] < self.end_pos[1]:
            pygame.draw.rect(sc, self.colour, pygame.Rect(self.start_pos[0], self.start_pos[1], side_length, side_length), self.size)
        elif self.start_pos[0] < self.end_pos[0] and self.start_pos[1] > self.end_pos[1]:
            pygame.draw.rect(sc, self.colour, pygame.Rect(self.start_pos[0], self.end_pos[1], side_length, side_length), self.size)
        elif self.start_pos[0] > self.end_pos[0] and self.start_pos[1] < self.end_pos[1]:
            pygame.draw.rect(sc, self.colour, pygame.Rect(self.end_pos[0], self.start_pos[1], side_length, side_length), self.size)
        elif self.start_pos[0] > self.end_pos[0] and self.start_pos[1] > self.end_pos[1]:
            pygame.draw.rect(sc, self.colour, pygame.Rect(self.end_pos[0], self.end_pos[1], side_length, side_length), self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for obj in drawings:
            obj.draw()

#Class to draw a circle
class Circle:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds the radius and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        radius = int(math.sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2))
        pygame.draw.circle(sc, self.colour, (self.start_pos[0], self.start_pos[1]), radius, self.size)
    
#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

#Class to draw a Right Triangle
class Right_Triangle:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds points of triangle and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        pygame.draw.polygon(sc, self.colour, ((self.start_pos[0], self.start_pos[1]), (self.start_pos[0], self.end_pos[1]), (self.end_pos[0], self.start_pos[1])), self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

#Class to draw an Equilateral Triangle
class Eqilateral_Triangle:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds points of triangle and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        dx = abs(self.end_pos[0] - self.start_pos[0])
        pygame.draw.polygon(sc, self.colour, ((self.start_pos[0] - dx, self.start_pos[1]), (self.start_pos[0], self.end_pos[1]), (self.start_pos[0] + dx, self.start_pos[1])), self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

#Class to draw a Rhombus
class Rhombus:
    def __init__(self, pos, colour, size):
        self.start_pos = pos
        self.end_pos = pos
        self.colour = colour
        self.size = size

#Finds points of rhombus and starting positions with the specified mouse position values and draws on the screen
    def draw(self):
        dx = abs(self.end_pos[0] - self.start_pos[0])
        dy = abs(self.end_pos[1] - self.start_pos[1])
        pygame.draw.polygon(sc, self.colour, ((self.start_pos[0] - dx, self.start_pos[1]), (self.start_pos[0], self.start_pos[1] - dy), (self.start_pos[0] + dx, self.start_pos[1]), (self.start_pos[0], self.start_pos[1] + dy)), self.size)

#Updates and retrieves the current mouse position, as well as redraws previous drawings
    def update(self, current_pos, drawings):
        sc.fill(WHITE)
        self.end_pos = current_pos
        for object in drawings:
            object.draw()

#Other Varaibles
button = Button()
shape = 'pen'
colour = BLACK
size = 1
drawings = []
objects = None
flStartDrawing = False
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN: #Checks the correspondence of the mouse position on the screen and pressing the buttons 
            #Selection of drawing tools
            if button.pen.collidepoint(pygame.mouse.get_pos()): shape = 'pen'
            elif button.square.collidepoint(pygame.mouse.get_pos()): shape = 'square'
            elif button.rect.collidepoint(pygame.mouse.get_pos()): shape = 'rect'
            elif button.circle.collidepoint(pygame.mouse.get_pos()): shape = 'circle'
            elif button.eraser.collidepoint(pygame.mouse.get_pos()): shape = 'eraser'
            elif button.right_triangle.collidepoint(pygame.mouse.get_pos()): shape = 'right_triangle'
            elif button.equilateral_triangle.collidepoint(pygame.mouse.get_pos()): shape = 'equilateral_triangle'
            elif button.rhombus.collidepoint(pygame.mouse.get_pos()): shape = 'rhombus'
            elif button.size_reduce.collidepoint(pygame.mouse.get_pos()): 
                if size > 1: size -= 1
            elif button.size_rise.collidepoint(pygame.mouse.get_pos()):
                if size < 6: size += 1

            #Selection of colours
            if button.red.collidepoint(pygame.mouse.get_pos()): colour = RED
            elif button.green.collidepoint(pygame.mouse.get_pos()): colour = GREEN
            elif button.blue.collidepoint(pygame.mouse.get_pos()): colour = BLUE
            elif button.black.collidepoint(pygame.mouse.get_pos()): colour = BLACK
            elif button.yellow.collidepoint(pygame.mouse.get_pos()): colour = YELLOW
            elif button.orange.collidepoint(pygame.mouse.get_pos()): colour = ORANGE
            elif button.pink.collidepoint(pygame.mouse.get_pos()): colour = PINK
            elif button.grey.collidepoint(pygame.mouse.get_pos()): colour = GREY

            #Defines objects value
            if shape == 'pen':
                object = Pen(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'square':
                object = Square(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'rect': 
                object = Rect(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'circle':
                object = Circle(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'eraser':
                object = Pen(pygame.mouse.get_pos(), WHITE, size * 10)
                flStartDrawing = True
            elif shape == 'right_triangle':
                object = Right_Triangle(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'equilateral_triangle':
                object = Eqilateral_Triangle(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
            elif shape == 'rhombus':
                object = Rhombus(pygame.mouse.get_pos(), colour, size)
                flStartDrawing = True
        #Draws objects on the screen when LBM pressed and mouse is moving
        if event.type == pygame.MOUSEMOTION and flStartDrawing:
            object.update(pygame.mouse.get_pos(), drawings)
            object.draw()
        #Stops draw when releases button
        if event.type == pygame.MOUSEBUTTONUP and shape != 'eraser':
            drawings.append(object)
            object = None
            flStartDrawing = False
        elif event.type == pygame.MOUSEBUTTONUP and shape == 'eraser':
            drawings.append(object)
            object = None
            flStartDrawing = False

    button.draw()
    pygame.display.update()


pygame.quit()