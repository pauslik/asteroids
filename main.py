import pygame
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        # Clear the screen
        screen.fill((0, 0, 0))
        # Update and draw the updatable objects
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        # Draw the drawable objects
        for sprite in drawable:
            sprite.draw(screen)
        # Update the display
        pygame.display.flip()
        #  Log the current state
        log_state()
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Cap the frame rate
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
