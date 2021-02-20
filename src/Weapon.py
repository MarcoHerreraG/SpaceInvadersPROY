import pygame
from BalasNORM import BalaNORM

class Weapon:
    def __init__(self):
        
        self.Balas = []
        self.count = 20 
        self.shoot_sound = pygame.mixer.Sound("Assets/Audio/Laser_Shoot.wav")
        self.Image2 = pygame.image.load("Assets/Image/Bala.png")
        
    
    def add_bullet(self):
        for i in range (self.count):
            bullet = BalaNORM(self.Image2)
            self.Balas.append(bullet)

    def update(self):
        for bullet in self.Balas:
            bullet.update()

    def draw(self, screen):
        for bullet in self.Balas:
            bullet.draw(screen)

    def shoot(self, x, y):
        self.add_bullet()        
        for bullet in self.Balas:
            if bullet.active == False:
                pygame.mixer.Sound.play(self.shoot_sound)
                bullet.rect.x = x
                bullet.rect.y = y
                bullet.active = True
                print(self.count)
                return
