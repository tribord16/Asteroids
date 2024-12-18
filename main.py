import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    running = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        
        pygame.Surface.fill(screen, (0,0,0))

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()
