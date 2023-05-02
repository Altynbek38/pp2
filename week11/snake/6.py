import pygame
import random

# Define constants for the game screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Define constants for the snake and food block sizes
BLOCK_SIZE = 10

# Define constants for the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the Snake class
class Snake:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.dx = BLOCK_SIZE
        self.dy = 0
        self.body = []
        self.length = 1
    
    def move(self):
        # Move the snake
        self.x += self.dx
        self.y += self.dy
        
        # Check for border collision
        if self.x < 0 or self.x >= SCREEN_WIDTH or self.y < 0 or self.y >= SCREEN_HEIGHT:
            return True
        
        # Check for body collision
        for block in self.body:
            if self.x == block[0] and self.y == block[1]:
                return True
        
        # Add the current position to the body
        self.body.append((self.x, self.y))
        
        # If the snake is longer than the allowed length, remove the oldest block
        if len(self.body) > self.length:
            self.body.pop(0)
        
        return False
    
    def draw(self, surface):
        # Draw the snake's head
        pygame.draw.rect(surface, GREEN, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        
        # Draw the snake's body
        for block in self.body:
            pygame.draw.rect(surface, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Define the Food class
class Food:
    def __init__(self):
        self.x, self.y = self.generate_random_position()
    
    def generate_random_position(self):
        # Generate a random position for the food
        while True:
            x = random.randrange(BLOCK_SIZE, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            y = random.randrange(BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            if (x, y) not in snake.body:
                return x, y
    
    def draw(self, surface):
        # Draw the food block
        pygame.draw.rect(surface, RED, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create the snake and food objects
snake = Snake()
food = Food()

# Initialize game variables
score = 0
level = 1
speed = 5
clock = pygame.time.Clock()
game_over = False

# Define the font for the score and level counters
font = pygame.font.SysFont('Arial', 18)

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -BLOCK_SIZE
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = BLOCK_SIZE