import pygame
import snake_class
import apple_class


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Creating the screen
    screen = pygame.display.set_mode((800, 640))

    # Title and Icon
    pygame.display.set_caption("Best Snake Ever")
    snake_icon = pygame.image.load("snake_icon.png")
    pygame.display.set_icon(snake_icon)

    # Creating objects
    player = snake_class.Snake()
    apple = apple_class.Apple()

    # Game loop
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Basic functions
        screen.fill((0, 0, 0))
        keys = snake_class.get_key()

        # Snake methods
        player.snake_head_move(keys)
        player.snake_body_move()
        player.snake_position_head(screen)
        player.snake_position_body(screen)

        # Apple methods
        apple.apple_spawn(screen)
        apple.apple_eat(player)

        # Update
        pygame.display.update()


if __name__ == "__main__":
    main()
