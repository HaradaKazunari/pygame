import numpy as np
import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('test')


    while True:
        screen.fill((0,0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == QUIT:
                pygame.quit()

if __name__ == '__main__':
    main()

