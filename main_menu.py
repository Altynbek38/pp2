import pygame
pygame.init()

monitor = pygame.display.set_mode((800, 800))

class Button:
    def __init__(self):
        self.rect_level1 = pygame.Rect(750, 50, 40, 40)#Позиция на экране
        self.rect_level2 = pygame.Rect(695, 50, 40, 40)
        self.rect_level3 = pygame.Rect(585, 50, 40, 40)
        self.image_level1 = pygame.image.load(r'image of level1')
        self.image_level2 = pygame.image.load(r'image of level2')
        self.image_level3 = pygame.image.load(r'image of level3')

    def draw(self):
        self.level1 = monitor.blit(self.image_level1, self.rect_level1)
        self.level2 = monitor.blit(self.image_level2, self.rect_level2)
        self.level3 = monitor.blit(self.image_level3, self.rect_level3)

clock = pygame.time.Clock()

button = Button()
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if button.level1.collidepoint(pygame.mouse.get_pos()): 
                execfile('путь/level1.py')
            elif button.level2.collidepoint(pygame.mouse.get_pos()): 
                pass #ССылка на Уровень 2
            elif button.level3.collidepoint(pygame.mouse.get_pos()): 
                pass #ССылка на Уровень 1
    
    button.draw()
    pygame.display.update()
    clock.tick(60)