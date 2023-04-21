import pygame
pygame.init()

W, H = 600, 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mouse options")

WHITE = (255, 255, 255)
GREEN = (0, 0, 255)
BLUE = (0, 255, 2)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H // 2
speed = 5

move = 0

flRunning = True

flStartDraw = False
sp = ep = None

sc.fill(WHITE)
pygame.display.update()

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flStartDraw:
                pos = event.pos
                width = abs(pos[0] - sp[0])
                height = abs(pos[1] - sp[1])

                sc.fill(WHITE)
                pygame.draw.rect(sc, RED, (min(sp[0],pos[0]), min(sp[1], pos[1]), width, height), 5)
                pygame.display.update()
               
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flStartDraw = False 
    clock.tick(FPS)