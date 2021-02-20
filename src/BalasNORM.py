from Balas import Bullet
class BalaNORM:
    def __init__(self):
        self.image = self.image.load("Assets\Image\Bullet.png")
        self.rect = self.image.get_rect()
        self.speed = 8        
        self.active = False
    
    def update(self):
        if self.active == True:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)