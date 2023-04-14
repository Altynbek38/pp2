import pygame
pygame.init()

W, H = 1366, 768

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Red Ball")

clock = pygame.time.Clock()
FPS = 60

x = W / 2
y = H / 2
RED = (255, 0, 0)
WHITE = (255, 255, 255)

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP] and y >= 25: y -= 20
    if pressed[pygame.K_DOWN] and y <= H - 25: y += 20
    if pressed[pygame.K_RIGHT] and x <= W - 25: x += 20
    if pressed[pygame.K_LEFT] and x >= 25: x -= 20

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()