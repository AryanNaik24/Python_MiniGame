import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# initialises pygame
pygame.init()

# sets the display caption to minigame
pygame.display.set_caption("MiniGame")


# declaring global variables

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

# sets window as a display
window = pygame.display.set_mode((WIDTH, HEIGHT))

# name is the color of bground


def getBackground(name):

    # loads image
    image = pygame.image.load(join("assets", "Background", name))

    # _ represents x and y coords which are to be ignored
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


# drawing all elements on the screen
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    # refreshes screen
    pygame.display.update()


def main(window):

    # clock ingame
    clock = pygame.time.Clock()

    # backgrounnd image
    background, bg_image = getBackground("Brown.png")

    # runs 60 frames per second . Helps regulate framerate
    run = True
    while (run):
        clock.tick(FPS)

        # quits if clicked on red cross top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # draws in the bg image
        draw(window, background, bg_image)

    pygame.quit()
    quit()


# only runs if file called directly
if __name__ == "__main__":
    main(window)
