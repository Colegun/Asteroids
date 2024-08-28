import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():

    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, all_asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
            for asteroid in all_asteroids:
                for bullet in shots:
                    if bullet.collision(asteroid):
                        bullet.kill()
                        asteroid.split()
                if asteroid.collision(player):
                    print("Game over!")
                    return
        pygame.Surface.fill(screen,(0, 0, 0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000
        


if __name__ == "__main__":
    main()