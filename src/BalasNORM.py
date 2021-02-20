from Balas import Bullet
class BalaNORM:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 1.1        
        self.active = False
    
    def update(self):
        if self.active == True:
            print("Salió bala")
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)