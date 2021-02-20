import pygame
from BalasNORM import BalaNORM

class Weapon:
    def __init__(self):
        
        self.Balas = []
        self.count = 20
        self.bullet_sprite = pygame.image.load("assets/images/bala_buena.png")    
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot_sound.wav")
            
    
    def add_bullet(self):
        for i in range (self.count):
            bullet = BalaNORM()
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
            if bullet.is_active == False:
                pygame.mixer.Sound.play(self.shoot_sound)
                bullet.rect.x = x
                bullet.rect.y = y
                bullet.is_active = True
                print(self.count)
                return
