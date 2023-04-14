import pygame
import datetime
pygame.init()

W, H = 829, 836

icon = pygame.image.load(r'C:\pp2\week10\images\icon.png')
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Clock")
pygame.display.set_icon(icon)

FPS = 6
clock = pygame.time.Clock()
time = datetime.datetime.now()
angle_s = -6 * int(time.strftime("%S"))
angle_m = -6 * (int(time.strftime("%M")) + 1)

mickey = pygame.image.load(r'C:\pp2\week10\images\bb.png')
left = pygame.image.load(r'C:\pp2\week10\images\left.png')
right = pygame.image.load(r'C:\pp2\week10\images\right.png')

screen.blit(mickey, (0, 0))

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    time = datetime.datetime.now()
    angle_s = -6 * int(time.strftime("%S"))
    angle_m = -6 * (int(time.strftime("%M")) + 1)

    rotated_right = pygame.transform.rotate(left, angle_s)
    rotated_left = pygame.transform.rotate(right, angle_m)

    right_rect = rotated_right.get_rect(center = left.get_rect(center = (W / 2, H / 2)).center)
    left_rect = rotated_left.get_rect(center = right.get_rect(center = (W / 2, H / 2)).center)

    screen.blit(mickey, (0, 0))
    screen.blit(rotated_left, left_rect)
    screen.blit(rotated_right, right_rect)
    
    angle_s -= 1
    pygame.display.update()
    clock.tick(FPS)