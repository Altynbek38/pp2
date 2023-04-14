import pygame
import os
pygame.init()
W, H = 600, 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()
FPS = 60

path = r'C:\Musics'
player = os.listdir(path)

MARINE = (180 ,210, 230)
WHITE = (255, 255, 255)

next = pygame.image.load(r'C:\pp2\week10\images\next_button.png')
pause = pygame.image.load(r'C:\pp2\week10\images\pause_button.png')
prev = pygame.image.load(r'C:\pp2\week10\images\prev_button.png')

index = 0
def play_music(index):
    pygame.mixer.music.load(os.path.join(path,  player[index]))
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_music(index):
    if index < len(player) - 1: index += 1
    else: index = 0
    return index

def prev_music(index):
    if index > 0: index -= 1
    else: index = len(player) - 1
    return index

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

font = pygame.font.SysFont('Arial', 20)
text = font.render(player[index], True, (0, 0, 0))
sc.blit(text, (10, 10))

cnt = 0
ok = True
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ok = True
                cnt += 1
                if cnt == 1: play_music(index)
                elif cnt % 2 == 0: pause_music()
                elif cnt % 2 == 1: unpause_music()
            elif event.key == pygame.K_ESCAPE:
                ok = False
                stop_music()
                cnt = 0
            elif event.key == pygame.K_RIGHT:
                ok = True
                if cnt % 2 == 0: cnt += 1
                index = next_music(index)
                play_music(index)
            elif event.key == pygame.K_LEFT:
                ok = True
                if cnt % 2 == 0: cnt += 1
                index = prev_music(index)
                play_music(index)
        if event.type == MUSIC_END and ok:
            index = next_music(index)
            play_music(index)
        

    sc.fill(WHITE)
    text = font.render(player[index], True, (0, 0, 0))
    sc.blit(prev, (200, 280))
    sc.blit(pause, (275, 275))
    sc.blit(next, (350, 280))
    sc.blit(text, (10, 250))
    pygame.display.update()
    clock.tick(FPS)    