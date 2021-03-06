import pygame

class ENEM():
    def __init__(self, x, y, fleet):
        self.screen = fleet.app.screen
        self.image = pygame.image.load ("Assets/Image/OrbeENEM.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.Xspeed = 0.5
        self.Yspeed = 0.1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, Orientacion):
        self.x += (self.Xspeed * Orientacion)
        self.y += self.Yspeed
        self.rect.x = self.x
        self.rect.y = self.y

    def Checar_Borde_INF(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def Checar_Bordes(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True