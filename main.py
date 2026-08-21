import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0

    # instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Allows the exit button in the game window to work
                return 

        screen.fill("black")

        # Render player and call update
        player.draw(screen) 
        player.update(dt)

        # Refreshes the screen
        pygame.display.flip()

        # Update the time clock
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
