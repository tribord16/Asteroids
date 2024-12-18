import pygame
from constants import *  # Import everything from constants.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # Directly use SCREEN_WIDTH
    print(f"Screen height: {SCREEN_HEIGHT}")  # Directly use SCREEN_HEIGHT

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.Surface.fill(screen, (255,255,255))
        pygame.display.flip()


if __name__ == "__main__":
    main()
