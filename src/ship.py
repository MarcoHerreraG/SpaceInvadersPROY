import pygame

class Ship:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("Assets/Image/Ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0.25
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.x + self.rect.width - 15 < self.screen_rect.width:
            self.x += self.speed     
        elif self.move_left and self.rect.x + 15 > 0:
            self.x -= self.speed
        self.rect.x = self.x