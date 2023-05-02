import pygame 

import random

pygame.init()

colors = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 190, 29),
    8192: (237, 187, 12),
    'light text': (249, 246, 242),
    'dark text': (119, 110, 101),
    'other': (0, 0, 0),
    'bg': (187, 173, 160) 
    }


w = 620
h = 800
monitor = pygame.display.set_mode((w,h))
matrix = [[0 for i in range(6)] for j in range(6)]
game_over = False
spawn_new = True
init_count = 0
direction = ''


pygame.display.set_caption('2048')

def cvadrat():
   pygame.draw.rect(monitor,[123,230,43],[0,0,620,620],0,5) 


def cvadrarici(matrix):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] > 0 and matrix[i][j] <= 8192:
                cvet = colors[matrix[i][j]]
            else:
                cvet = colors['dark text']
            pygame.draw.rect(monitor,cvet,[(i * 100) + 20, (j * 100) + 20,80,80],0,10)
            if matrix[i][j] > 0:
                #print("helooooo")
                font = pygame.font.Font('freesansbold.ttf',50 - (5 * len(str(matrix[i][j]))))
                value_text = font.render(str(matrix[i][j]),True,(0,0,0)) 
                text_rect = value_text.get_rect(center=(i * 100 + 60, j * 100 + 60))

                monitor.blit(value_text, text_rect)

def new_cvadratici(matrix):
    count = 0
    full = False
    while any(0 in row for row in matrix) and count < 1:
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        if matrix[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                matrix[row][col] = 4
            else:
                matrix[row][col] = 2
    if count < 1:
        full = True
    return matrix, full    
 

def direct(d,matrix):
    rowl = []
    if d == 'LEFT':
        for row in matrix:
            while 0 in row:
                row.remove(0)
            while len(row) != 6:
                row.append(0)
            for i in range(6):
                for j in range(5):
                    if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                        matrix[i][j] = matrix[i][j] * 2
                        matrix[i].pop(j + 1)
                        matrix[i].append(0)

    # if d == 'RIGHT':
    #     for row in matrix:
    #         while 0 in row:
    #             row.remove(0)
    #         while len(row) != 6:
    #             row.insert(0,0)
    #     for i in range(6):
    #         for j in range(5,0,-1):
    #                 if matrix[i][j] == matrix[i][j - 1] and matrix[i][j] != 0:
    #                     matrix[i][j] = matrix[i][j] * 2
    #                     matrix[i].pop(j - 1)
    #                     matrix[i].insert(0,0)

    if d == 'RIGHT':
# Get the number of rows and columns in the matrix
        num_rows = len(matrix)
        num_cols = len(matrix[0])

# Loop over the columns and check if each column consists only of 0s
        cols_to_delete = []
        for j in range(num_cols):
            all_zeros = True
            for i in range(num_rows):
                if matrix[i][j] != 0:
                    all_zeros = False
                    break
            if all_zeros:
                cols_to_delete.append(j)

# Delete the columns from the matrix
        cols_to_delete.sort(reverse=True) # delete columns from right to left
        for j in cols_to_delete:
            for i in range(num_rows):
                del matrix[i][j]
        for i in range(5):
            for j in range(5,1,-1):
                    if matrix[i][j] == matrix[i][j - 1] and matrix[i][j] != 0:
                        matrix[i][j] = matrix[i][j] * 2
                        matrix[i].pop(j - 1)
                        matrix[i].insert(0,0)

    # if d == 'DOWN':
    #     for i in range(6):
    #         for j in range(6):
    #               for l in range(6):
    #                 if l == 5:
    #                     while 0 in=:
    #                         row.remove(0)
    #                     while len(row) != 6:
    #                         row.insert(0,0)                             

    return matrix

check = True    

while check:
    monitor.fill('gray')
    cvadrat()
    cvadrarici(matrix)
    if spawn_new or init_count < 2:
        matrix, game_over = new_cvadratici(matrix)
        spawn_new = False
        init_count += 1
    if direction != '':
        matrix = direct(direction,matrix)
        direction = ''
        spawn_new = True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'
                
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'