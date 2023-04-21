#Imports
import pygame
import time
import random
pygame.init()

#Display options
W, H = 400, 600
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer")
background = pygame.image.load(r'C:\pp2\week12\racer\images\AnimatedStreet.png')

#Tick Rate
clock = pygame.time.Clock()
FPS = 60

#Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Other Variables
BG_POS = 0
C1_COLLIDE = False
C2_COLLIDE = False
COIN = 0
SPEED = 5
SCORE = 0
C1_SPEED = 6
C2_SPEED = 7
SPEED_TRACKER = 0

#Set Font
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, BLACK)

#Background Music
pygame.mixer.music.load(r'C:\pp2\week12\racer\sounds\background.wav')
pygame.mixer.music.play(-1)

#Classes of cars and coin
class Enemy(pygame.sprite.Sprite):
#Initialize enemy settings and generate them at the first take in a random position along x-asix
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\pp2\week12\racer\images\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
#Moves along the y axis at a given speed, if the back of the enemy car reaches the bottom of the screen, it is generated again and the player gets a point.
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, W - 30), -100)
#Draws an enemy car on the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
#Initialize the settings of the player's car and generate it in the specified position
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\pp2\week12\racer\images\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (W / 2, 520)
#Moves by player's commands on the x-axis
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 0: self.rect.move_ip(0, -10)
        if pressed[pygame.K_DOWN] and self.rect.bottom < H: self.rect.move_ip(0, 10)
        if pressed[pygame.K_LEFT] and self.rect.left > 0: self.rect.move_ip(-10, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < W: self.rect.move_ip(10, 0)
#Draws the player's car on the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin_1(pygame.sprite.Sprite):
#Initializes coin settings and generates them randomly along the x axis
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\pp2\week12\racer\images\Coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, W - 30), 0)
#Moves the coin along the y axis, also checks for screen borders and collision with the player's car
    def move(self):
        global C1_COLLIDE
        self.rect.move_ip(0, C1_SPEED)
        if C1_COLLIDE:
            self.rect.center = (random.randint(30, W - 30), -100)
            C1_COLLIDE = False

        if self.rect.top > 600:
            self.rect.center = (random.randint(30, W - 30), 0)

class Coin_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\pp2\week12\racer\images\Money.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, W - 30), -250)

    def move(self):
        global C2_COLLIDE
        self.rect.move_ip(0, C2_SPEED)
        if C2_COLLIDE:
            self.rect.center = (random.randint(30, W - 30), -500)
            C2_COLLIDE = False
        
        if self.rect.top > 600:
            self.rect.center = (random.randint(30, W - 30), -500)

#Draws a coin on the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
#Creating Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin_1()
C2 = Coin_2()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(C2)
      
#Main Loop
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
    
    if SPEED_TRACKER >= 10:
        SPEED += 1
        SPEED_TRACKER -= 10

    score = font_small.render(f'SCORE: {SCORE}', True, BLACK)
    sc.blit(background, (0, BG_POS)) 
    sc.blit(background, (0, BG_POS - 600))

    BG_POS += SPEED - 1
    if BG_POS >= 600:
        BG_POS = 0

    sc.blit(score, (10, 10))
    sc.blit(C1.image, C1.rect)
#Blits and uses the move function for all objects: enemy car, player car and coins
    for car in all_sprites:
        sc.blit(car.image, car.rect)
        car.move()
# Checks the collision of the player's car with a coin, if it becomes true, the player gets points in the form of a coin, also increases the speed of coins
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound(r'C:\pp2\week12\racer\sounds\coin.wav').play()
        if pygame.sprite.collide_rect(P1, C1):
            C1_COLLIDE = True
            C1_SPEED += 0.2
            COIN += 1
            SPEED_TRACKER += 1
            C1.move()
        if pygame.sprite.collide_rect(P1, C2):
            C2_COLLIDE = True
            C2_SPEED += 0.2
            COIN += 5
            SPEED_TRACKER += 5
            C2.move()       

    coin = font_small.render(f'COINS: {COIN}', True, BLACK)
    sc.blit(coin, (275, 10))
# Checks the collision of the player's car with the opponent's car, if this becomes true, the game will end
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\pp2\week12\racer\sounds\crash.wav').play()
        time.sleep(0.5)
        sc.fill(RED)
        sc.blit(game_over, (30, 250))
        pygame.display.update()
        for car in all_sprites:
            car.kill()
        time.sleep(2)
        flRunning = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()   