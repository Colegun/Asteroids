import pygame
from constants import *
from circleshape import *
from player import *

def main():

    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000
        


if __name__ == "__main__":
    main()