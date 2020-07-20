import pygame
import sys
import random

"""
    Pygame documentation
    https://www.pygame.org/docs/
"""
pygame.init()

WIDTH = 800
HEIGHT = 600

SPEED = 10

player_size = 50
# positioning the player block at the botom-middle of the screen
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]

COLOUR = [(255,0,0), (0,0,255)]
BACKGROUND_COLOUR = (0,0,0)


# defining the screen and its size to display the game on.
screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

# setting the framerate of the display
clock = pygame.time.Clock()

while not game_over:
    # pygame is an event based library. We can access the events that take place
    # within the display
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        # making use of keystrokes input by the player
        if event.type == pygame.KEYDOWN:
            # unpacking the player position list to make mods. simpler
            x = player_pos[0]
            y = player_pos[1]

            # altering player position based on the key pressed
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            # updating the position of the player
            player_pos = [x,y]


    # we fill the background with black colour since the movement of the player block leaves a trail of whatever colourthe player is.
    # this way, it appears as though the block moves completely without leaving a trace.
    screen.fill(BACKGROUND_COLOUR)

    # here we drop the enemy blocks from the top of the screen to the bottom
    # the amount the block moves down is determined by the SPEED
    # once it reaches the bottom ie pos = HEIGHT, the block pos. is reset to the top.
    # we also add a random x location so it starts from a random spot each time.
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += SPEED
    else:
        enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
        enemy_pos[1] = 0


    # here we create the player and enemy blocks ie the one that is controlled by the players and the AI
    # args order: display screen obj, colour of the rectangle, a tuple of obj positions on screen and sizes (left, top, width, height)
    pygame.draw.rect(screen, COLOUR[1], (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, COLOUR[0], (player_pos[0],player_pos[1], player_size,player_size))

    # setting framerate to 30 fps
    clock.tick(30)

    # after creating the objects above, the display needs to be updated each time.
    pygame.display.update()
