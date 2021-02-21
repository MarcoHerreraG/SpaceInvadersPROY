import pygame
from Weapon import Weapon

class Ship:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("Assets/Image/Ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 1
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False
        self.Weapon = Weapon()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.Weapon.draw(self.screen)

    def update(self):
        if self.move_right and self.rect.x + self.rect.width - 20 < self.screen_rect.width:
            self.speed = 1
            self.x += self.speed     
        elif self.move_left and self.rect.x + 15 > 0:
            self.speed = 1
            self.x -= self.speed
        self.rect.x = self.x
        self.Weapon.update()

    def Disparar(self):
        self.Weapon.shoot(self.rect.x + 18, self.rect.y)

    def DispararESP(self, Puntuacion):
        if(Puntuacion >= 4):
            self.Weapon.shootESP(self.rect.x+18, self.rect.y)