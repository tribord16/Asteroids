import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

def main():
    ## VARIABLES ##
    dt = 0
    running = True
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = {shots, updatable, drawable}
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()


    ## DEBUT DU JEU ##
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if(asteroid.check_collisions(player)): 
                print("Game OVER - TRIBORD")
                running = False
            for bullet in shots:
                if(asteroid.check_collisions(bullet)):
                    bullet.kill()
                    asteroid.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()
