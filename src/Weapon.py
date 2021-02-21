import pygame
from BalasNORM import BalaNORM
from BalasESP import BalaESP

class Weapon:
    def __init__(self):
        
        self.Balas = []
        self.Balas2 = []
        self.count = 10 
        self.countEspecial = 2
        self.shoot_sound = pygame.mixer.Sound("Assets/Audio/Laser_Shoot.wav")
        self.Image = pygame.image.load("Assets/Image/BalaESP.png")
        self.Image2 = pygame.image.load("Assets/Image/Bala.png")
    
    def add_bullet(self):
        for i in range (self.count):
            bullet = BalaNORM(self.Image2)
            self.Balas.append(bullet)

    def add_bulletESP(self):
        for i in range (self.countEspecial):
            bullet = BalaESP(self.Image)
            self.Balas2.append(bullet)

    def update(self):
        for bullet in self.Balas:
            bullet.update()
        for bullet in self.Balas2:
            bullet.update()

    def draw(self, screen):
        for bullet in self.Balas:
            bullet.draw(screen)
        for bullet in self.Balas2:
            bullet.draw(screen)

    def shoot(self, x, y):
        if len(self.Balas) < 1:
            self.add_bullet()
        for bullet in self.Balas:
            if bullet.active == False:
                pygame.mixer.Sound.play(self.shoot_sound)
                bullet.rect.x = x
                bullet.rect.y = y
                bullet.active = True
                return

    def shootESP(self, x, y):
        if len(self.Balas2) < 1:
            self.add_bulletESP()
        for bullet in self.Balas2:
            if bullet.active == False:
                pygame.mixer.Sound.play(self.shoot_sound)
                bullet.rect.x = x
                bullet.rect.y = y
                bullet.active = True
                return
