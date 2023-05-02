import pygame

pygame.init()
clock = pygame.time.Clock()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pause Example")

# Set up the font
font = pygame.font.SysFont(None, 50)

# Set up the game state
paused = False

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    # Draw the screen
    screen.fill((255, 255, 255))
    if paused:
        text = font.render("Paused", True, (0, 0, 0))
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)