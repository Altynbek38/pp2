#Import 
import random
import pygame
pygame.init()

#Dispaly Settings
W, H = 800, 800
SIZE = 40
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake')

#Tick Rate
clock = pygame.time.Clock()
FPS = 10

#Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Other Variables
locked = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': True}
SCORE = 0
dx = 0
dy = 0

#Grid Function
def grid():
    for x in range(0, W, SIZE):
        for y in range(0, H, SIZE):
            rect = pygame.Rect(x, y, SIZE, SIZE)
            pygame.draw.rect(sc, (50, 50, 50), rect, 1)

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food:
    def __init__(self):
        self.location = Point(random.randint(1, W / SIZE - 1), random.randint(1, H / SIZE - 1))
    
    def draw(self):
        rect = pygame.Rect(self.location.x * SIZE, self.location.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, RED, rect)

class Snake:
    def __init__(self):
        self.x = 11
        self.y = 10
        self.snake = [Point(self.x, self.y)]
    
    def move(self):
        if self.snake[0].x * SIZE < 0: self.snake[0].x = W / SIZE
        if self.snake[0].x * SIZE > W: self.snake[0].x = 0
        if self.snake[0].y * SIZE < 0: self.snake[0].y = H / SIZE
        if self.snake[0].y * SIZE > H: self.snake[0].y = 0

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].x = self.snake[i - 1].x
            self.snake[i].y = self.snake[i - 1].y
        
        self.snake[0].x += dx
        self.snake[0].y += dy
    
    def draw(self):
        rect = pygame.Rect(self.snake[0].x * SIZE, self.snake[0].y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, WHITE, rect)

        for i in range(1, len(self.snake) - 1):
            rect = pygame.Rect(self.snake[i].x * SIZE, self.snake[i].y * SIZE, SIZE, SIZE)
            pygame.draw.rect(sc, GREEN, rect)
    
    def check_collision(self, food):
        global SCORE
        if self.snake[0].x == food.location.x and self.snake[0].y == food.location.y:
            SCORE += 1
            self.snake.append(Point(food.location.x, food.location.y))
            food.location = Point(random.randint(1, W / SIZE - 1), random.randint(1, H / SIZE - 1))
        for i in range(1, len(self.snake) - 1):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                print('loh')


food = Food()
snake = Snake()


flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and locked['UP']:
                locked = {'UP': True, 'DOWN': False, 'RIGHT': True, 'LEFT': True}
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN and locked['DOWN']:
                locked = {'UP': False, 'DOWN': True, 'RIGHT': True, 'LEFT': True}
                dx = 0
                dy = 1
            elif event.key == pygame.K_RIGHT and locked['RIGHT']:
                locked = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': False}
                dx = 1
                dy = 0
            elif event.key == pygame.K_LEFT and locked['LEFT']:
                locked = {'UP': True, 'DOWN': True, 'RIGHT': False, 'LEFT': True}
                dx = -1 
                dy = 0
    sc.fill(BLACK)
    snake.draw()
    food.draw()
    snake.move()
    snake.check_collision(food)
    grid()
    pygame.display.update()
    clock.tick(FPS)