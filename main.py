import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gametime = pygame.time.Clock()
    dt = 0

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = gametime.tick(60)


if __name__ == "__main__":
    main()
