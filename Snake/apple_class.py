import pygame
import random

pygame.init()


class Apple:
    apple = pygame.image.load("apple.png")
    apple_x = int(random.randint(0, 768))
    apple_y = int(random.randint(0, 608))

    def apple_spawn(self, screen):
        screen.blit(self.apple, (self.apple_x, self.apple_y))

    def apple_eat(self, player):
        # Doesnt work too well yet
        if player.snake_head_x == self.apple_x or player.snake_head_y == self.apple_y:
            self.apple_x = int(random.randint(0, 768))
            self.apple_y = int(random.randint(0, 608))
            player.body_parts += 1
