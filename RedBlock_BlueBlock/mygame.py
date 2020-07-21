import pygame
import sys
import random

"""
    Pygame documentation
    https://www.pygame.org/docs/
"""
pygame.init()

# VARIABLE INITIALISATIONS:
WIDTH = 800
HEIGHT = 600

# controls how fast the enemy blocks are dropped
SPEED = 10

PLAYER_SIZE = 50
# positioning the player block at the botom-middle of the screen
PLAYER_POS = [WIDTH/2, HEIGHT-2*PLAYER_SIZE]

ENEMY_SIZE = 50
ENEMY_POS = [random.randint(0, WIDTH-ENEMY_SIZE), 0]
enemy_list = [ENEMY_POS]

COLOUR = [(255,0,0), (0,0,255), (255,255,0)]
BACKGROUND_COLOUR = (0,0,0)

# defining the screen and its size to display the game on.
screen = pygame.display.set_mode((WIDTH,HEIGHT))

SCORE = 0
GAME_OVER = False

myFont = pygame.font.SysFont('monospace', 35, bold=True)

# setting the framerate of the display
clock = pygame.time.Clock()

# GAME FUNCTIONS:
def create_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        enemy_x_pos = random.randint(0, WIDTH-ENEMY_SIZE)
        enemy_y_pos = 0
        enemy_list.append([enemy_x_pos, enemy_y_pos])

def draw_enemies(enemy_list):
    for ENEMY_POS in enemy_list:
        pygame.draw.rect(screen, COLOUR[1], (ENEMY_POS[0], ENEMY_POS[1], ENEMY_SIZE, ENEMY_SIZE))

def drop_enemies(enemy_list):
    # here we drop the enemy blocks from the top of the screen to the bottom
    # the amount the block moves down is determined by the SPEED
    # once it reaches the bottom ie pos = HEIGHT, the block pos. is reset to the top.
    # we also add a random x location so it starts from a random spot each time.
    for index, ENEMY_POS in enumerate(enemy_list):
        global SCORE
        if ENEMY_POS[1] >= 0 and ENEMY_POS[1] < HEIGHT:
            ENEMY_POS[1] += SPEED
        else:
            # if the block reaches the bottom of the screen
            # we remove it from the list. The create enemy func.
            # will then create another block at a random position.
            enemy_list.pop(index)
            # if the enemy blocks reach the bottom, update score
            SCORE += 1

def collisions(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collisions(player_pos, enemy_pos):
            return True
    return False

def detect_collisions(PLAYER_POS, ENEMY_POS):

    player_x = PLAYER_POS[0]
    player_y = PLAYER_POS[1]

    enemy_x = ENEMY_POS[0]
    enemy_y = ENEMY_POS[1]

    # detecting any overlap in the x axis:
    if (player_x >= enemy_x and player_x < (enemy_x+ENEMY_SIZE)) or (enemy_x > player_x and enemy_x < (player_x+PLAYER_SIZE)):
        if (player_y >= enemy_y and player_y < (enemy_y+ENEMY_SIZE)) or (enemy_y > player_y and enemy_y < (player_y+PLAYER_SIZE)):

            return True

    return False

def set_level(score):
    global SPEED
    if score < 10:
        SPEED = 5
    elif score < 20:
        SPEED = 8
    elif score < 30:
        SPEED = 12
    elif score < 50:
        SPEED = 20


# Main Game
while not GAME_OVER:
    # pygame is an event based library. We can access the events that take place
    # within the display
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        # making use of keystrokes input by the player
        if event.type == pygame.KEYDOWN:
            # unpacking the player position list to make mods. simpler
            x = PLAYER_POS[0]
            y = PLAYER_POS[1]

            # altering player position based on the key pressed
            if event.key == pygame.K_LEFT:
                x -= PLAYER_SIZE
            elif event.key == pygame.K_RIGHT:
                x += PLAYER_SIZE

            # updating the position of the player
            PLAYER_POS = [x,y]

    # we fill the background with black colour since the movement of the player block leaves a trail of whatever colourthe player is.
    # this way, it appears as though the block moves completely without leaving a trace.
    screen.fill(BACKGROUND_COLOUR)

    create_enemies(enemy_list)
    drop_enemies(enemy_list)

    text = "Score:" + str(SCORE)
    label = myFont.render(text, 1, COLOUR[2])
    screen.blit(label, (WIDTH-200, HEIGHT-40))

    set_level(SCORE)

    # detecting collisions over all the enemy blocks
    # this func. calls the detect_collisions func. to
    # determine if there is any collision.
    if collisions(enemy_list, PLAYER_POS):
        GAME_OVER = True
        break

    draw_enemies(enemy_list)

    # here we create the player block ie the one that is controlled by the players - the enemy blocks are created in the function.
    # args order: display screen obj, colour of the rectangle, a tuple of obj positions on screen and sizes (left, top, width, height)
    pygame.draw.rect(screen, COLOUR[0], (int(PLAYER_POS[0]),int(PLAYER_POS[1]), PLAYER_SIZE,PLAYER_SIZE))

    # setting framerate to 30 fps
    clock.tick(30)

    # after creating the objects above, the display needs to be updated each time.
    pygame.display.update()
