#Imports and initializing
import random
import time
import pygame
import psycopg2
from config import config
pygame.init()

def create_tables():
    commands = (
        """CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(50) UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_scores (
            user_id SERIAL PRIMARY KEY,
            score INT,
            level INT,
            FOREIGN KEY (user_id)
            REFERENCES users (user_id)
        )
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_data(username, score, level):
    sql = """INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
        user_id = cur.fetchone()[0]
        cur.execute(sql, (user_id, score, level))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_data(username, score, level):
    sql = """UPDATE user_scores
        SET score = %s,
            level = %s
        WHERE user_id = %s
        """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
        user_id = cur.fetchone()[0]
        cur.execute(sql, (score, level, user_id))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
is_new = False
print("Welcome to the Snake game!")
create_tables()
conn = None
try:
    parser = config()
    conn = psycopg2.connect(**parser)
    cur = conn.cursor()
    username = input("Enter your username: ")
    cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
    user_id = cur.fetchone()
    if user_id is None:
        is_new = True
        cur.execute("""INSERT INTO users (user_name) VALUES (%s) RETURNING user_id""", (username,))
        user_id = cur.fetchone()[0]
        print("New user created with user_id:", user_id)
        conn.commit()
    else:
        cur.execute("SELECT level FROM user_scores WHERE user_id = %s", (user_id,))
        current_level = cur.fetchone()[0]
        cur.execute("SELECT score FROM user_scores WHERE user_id = %s", (user_id,))
        current_score = cur.fetchone()[0]
        print(f"Welcome back! Your current level is: {current_level} and your score is {current_score}")
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

#Display settings
W, H = 800, 800
SIZE = 40
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

#Tick Rate
clock = pygame.time.Clock()
FPS = 6

#Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Font
font_big = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font_big.render("Game Over", True, RED) 

#Other Varaibles
SCORE = 0
SPEED = 5
level_score = 0
total_score = 0
score_track = 0
LEVEL = 0
dx, dy = 0, 0
locked_keys = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

#Grid Draw function
def grid():
    for x in range(0, W, SIZE):
        for y in range(0, H, SIZE):
            rect = pygame.Rect(x, y, SIZE, SIZE)
            pygame.draw.rect(sc, (50, 50, 50), rect, 1)

#Class Point to strore two variables like one
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
#Class Wall takes notes from txt file and builts walls in game screen
class Wall:
    def __init__(self, LEVEL):
        self.wall = []
        self.LEVEL = LEVEL
        f = open("C:\pp2\week11\snake\level{}.txt".format(self.LEVEL), "r")
#appending wall point to list
        for y in range(0, H // SIZE + 1):
            for x in range(0, W // SIZE + 1):
                if f.read(1) == '#':
                    self.wall.append(Point(x, y))
#draw function draws walls on the screen
    def draw(self):
        for point in range(0, len(self.wall) - 1):
            rect = pygame.Rect(self.wall[point].x * SIZE, self.wall[point].y * SIZE, SIZE, SIZE)
            pygame.draw.rect(sc, BLUE, rect)

#Class Food where function generate generates food randomly and draw function draws food on the plane
class Food:
    def __init__(self):
        self.location = []
#generate_food function generates food randomly
    def generate_food(self, S1, L1):
        running = True
        while running:
            running = False
            self.location = Point(random.randint(0, W / SIZE - 1), random.randint(0, H / SIZE - 1))
            for i in range(len(S1.snake)):
                if self.location.x == S1.snake[i].x and self.location.y == S1.snake[i].y:
                    running = True
            for i in range(len(L1.wall)):
                if self.location.x == L1.wall[i].x and self.location.y == L1.wall[i].y:
                    running = True
#draw function draws food on the screen
    def draw(self):
        rect = pygame.Rect(self.location.x * SIZE, self.location.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, RED, rect)

class Food_Big:
    def __init__(self):
        self.location = []
    
    def generate_food(self, S1, L1):
        running = True
        while running:
            running = False
            self.location = Point(random.randint(0, W / SIZE - 1), random.randint(0, H / SIZE - 1))
            for i in range(len(S1.snake)):
                if self.location.x == S1.snake[i].x and self.location.y == S1.snake[i].y:
                    running = True
            for i in range(len(L1.wall)):
                if self.location.x == L1.wall[i].x and self.location.y == L1.wall[i].y:
                    running = True
    
    def draw(self):
        rect = pygame.Rect(self.location.x * SIZE, self.location.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, GREEN, rect)

#Snake class
class Snake:
    def __init__(self):
        self.x = 10
        self.y = 11
        self.snake =[Point(self.x, self.y)]
#move function: moves the snake in the for loop, iterates the snake from tail to head, each segment takes positions in front of them
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].x = self.snake[i - 1].x
            self.snake[i].y = self.snake[i - 1].y
        
        self.snake[0].x += dx
        self.snake[0].y += dy
        
        if self.snake[0].x * SIZE> W: self.snake[0].x = 0
        if self.snake[0].x * SIZE< 0: self.snake[0].x = W / SIZE
        if self.snake[0].y * SIZE> H: self.snake[0].y = 0
        if self.snake[0].y * SIZE< 0: self.snake[0].y = H / SIZE
#draw function draws a snake on the screen
    def draw(self):
        point = self.snake[0]
        rect = pygame.Rect(point.x * SIZE, point.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, WHITE, rect)
        for point in self.snake[1:]:
            rect = pygame.Rect(point.x * SIZE, point.y * SIZE, SIZE, SIZE)
            pygame.draw.rect(sc, GREEN, rect)

#check_collision function: check the position of the snake's head relative to the food, the wall and its body. 
#If the snakehead collides with food, its length will increase by 1 point, otherwise the game will be over
    def check_collision(self, S1, F1, L1, F2):
        global username
        global is_new
        global total_score
        global SCORE
        global score_track
        global flag_score
#Checks if the snake's head has collided with food
        if self.snake[0].x == F1.location.x and self.snake[0].y == F1.location.y:
            self.snake.append(Point(F1.location.x, F1.location.y))
            SCORE += 1
            total_score += 1
            score_track += 1
            F1.generate_food(S1, L1)

        if self.snake[0].x == F2.location.x and self.snake[0].y == F2.location.y:
            if locked_keys == {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}:
                self.snake.append(Point(F2.location.x, F2.location.y - 1))
            elif locked_keys == {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}:
                self.snake.append(Point(F2.location.x, F2.location.y + 1))
            elif locked_keys == {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}:
                self.snake.append(Point(F2.location.x + 1, F2.location.y))
            elif locked_keys == {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}:
                self.snake.append(Point(F2.location.x - 1, F2.location.y))
            self.snake.append(Point(F2.location.x, F2.location.y))
            SCORE += 2
            total_score += 2
            flag_score = False
            F2.location = Point(-10, -10)
#Checs if the snake's head has collided with its body
        for i in range(1, len(self.snake) - 1):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                sc.blit(game_over, (220, 240))
                sc.blit(score, (340, 360))
                sc.blit(level, (340, 380))
                pygame.display.update()
                if is_new: insert_data(username, total_score + 1, level_score)
                else: update_data(username, total_score + 1, level_score)
                time.sleep(2)
                pygame.quit()
#Checs if the snake's head has collided with wall
        for i in range(0 ,len(L1.wall) - 1):
            if self.snake[0].x == L1.wall[i].x and self.snake[0].y == L1.wall[i].y:
                sc.blit(game_over, (220, 240))
                sc.blit(score, (340, 360))
                sc.blit(level, (340, 380))
                pygame.display.update()
                if is_new: insert_data(username, total_score, level_score + 1)
                else: update_data(username, total_score, level_score + 1)
                time.sleep(2)
                pygame.quit()

S1 = Snake()
L1 = Wall(LEVEL)
F1 = Food()
F2 = Food_Big()
F1.generate_food(S1, L1)
F2.generate_food(S1, L1)
F2.location = Point(-10, -10)

FOOD_END = pygame.USEREVENT + 1

#Main Loop
flag = False
flag_score = False
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.KEYDOWN: #Accepts pressed keys from the user and works with them, also blocks the opposite type of movement
            if event.key == pygame.K_UP and locked_keys['UP']:
                locked_keys = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
                dy = -1
                dx = 0
            elif event.key == pygame.K_DOWN and locked_keys['DOWN']:
                locked_keys = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                dy = 1
                dx = 0
            elif event.key == pygame.K_LEFT and locked_keys['LEFT']:
                locked_keys = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
                dy = 0
                dx = -1
            elif event.key == pygame.K_RIGHT and locked_keys['RIGHT']:
                locked_keys = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
                dy = 0
                dx = 1
        if event.type == FOOD_END and flag_score:
            F2.location = Point(-10, -10)
#Next level
    if SCORE > 10:
        level_score += 1
        LEVEL += 1
        FPS += 1
        if LEVEL == 4:
            LEVEL = 0
        SCORE = 0
        sc.fill(BLACK)
        L1.draw()
        S1.draw()
        L1 = Wall(LEVEL)
        S1 = Snake()
        F1.generate_food(S1, L1)
        grid()
        pygame.display.update()
        flag = True
    if score_track >= 4:
        F2.generate_food(S1, L1)
        pygame.time.set_timer(FOOD_END, 5000)
        score_track = 0
        flag_score = True
#Working with display
    sc.fill(BLACK)
    score = font_small.render(f'SCORE: {total_score}', True, WHITE)
    level = font_small.render(f'LEVEL: {level_score + 1}', True, WHITE)
    S1.check_collision(S1, F1, L1, F2)
    S1.move()
    F1.draw()
    if flag_score:
        F2.draw()
    S1.draw()
    L1.draw()
    grid()
    sc.blit(score, (10, 10))
    sc.blit(level, (700, 10))
    pygame.display.update()
    clock.tick(FPS)
    if flag:
        flag = False
        time.sleep(1)
pygame.quit()

conn.commit()
cur.close()
conn.close()