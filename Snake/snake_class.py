import pygame

pygame.init()


# Snake class
def get_key():
    keys = pygame.key.get_pressed()

    return keys


class Snake:
    snake_head = pygame.image.load("snake_head.jpg")
    snake_body = pygame.image.load("snake_body.jpg")

    snake_head_x = 368
    snake_head_y = 298
    snake_head_change_x = 0
    snake_head_change_y = -1

    body_parts = 1
    snake_body_x = snake_head_x
    snake_body_y = snake_head_y + 35
    snake_body_change_x = 0
    snake_body_change_y = -1

    def snake_position_head(self, screen):
        screen.blit(self.snake_head, (self.snake_head_x, self.snake_head_y))

    def snake_position_body(self, screen):
        screen.blit(self.snake_body, (self.snake_body_x, self.snake_body_y))

    def snake_head_move(self, keys):
        self.snake_head_x += self.snake_head_change_x
        self.snake_head_y += self.snake_head_change_y

        if self.snake_body_y == self.snake_head_y:
            if keys[pygame.K_UP]:
                self.snake_head_change_y = -1
                self.snake_head_change_x = 0
            elif keys[pygame.K_DOWN]:
                self.snake_head_change_y = 1
                self.snake_head_change_x = 0
        elif self.snake_body_x == self.snake_head_x:
            if keys[pygame.K_LEFT]:
                self.snake_head_change_x = -1
                self.snake_head_change_y = 0
            elif keys[pygame.K_RIGHT]:
                self.snake_head_change_x = 1
                self.snake_head_change_y = 0

        if self.snake_head_x >= 784:
            self.snake_head_x = 784
        elif self.snake_head_x <= 0:
            self.snake_head_x = 0
        elif self.snake_head_y >= 624:
            self.snake_head_y = 624
        elif self.snake_head_y <= 0:
            self.snake_head_y = 0

    def snake_body_move(self):
        self.snake_body_y += self.snake_body_change_y
        self.snake_body_x += self.snake_body_change_x

        if self.snake_body_y != self.snake_head_y and self.snake_body_x == self.snake_head_x:
            if self.snake_head_change_y == -1:
                self.snake_body_change_y = -1
                self.snake_body_change_x = 0
            elif self.snake_head_change_y == 1:
                self.snake_body_change_y = 1
                self.snake_body_change_x = 0

        elif self.snake_body_x != self.snake_head_x and self.snake_body_y == self.snake_head_y:
            if self.snake_head_change_x == -1:
                self.snake_body_change_x = -1
                self.snake_body_change_y = 0
            elif self.snake_head_change_x == 1:
                self.snake_body_change_x = 1
                self.snake_body_change_y = 0

        if self.snake_body_x >= 781:
            self.snake_body_x = 784
        elif self.snake_body_x <= 0:
            self.snake_body_x = 0
        elif self.snake_body_y >= 621:
            self.snake_body_y = 624
        elif self.snake_body_y <= 0:
            self.snake_body_y = 0
