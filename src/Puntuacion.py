import pygame

class Puntuacion:
    def __init__(self, app):
        
        self.screen = app.screen
        self.Puntos = 0
    def draw(self):
        self.screen.blit(self.score_letters, self.score_rect)

    def update(self):
        self.font=pygame.font.Font("Assets/Fonts/papercut.ttf", 32)
        self.score_letters = self.font.render("Puntos : %d " % (self.Puntos), True, (255,255,255))
        self.score_rect = self.score_letters.get_rect()
        self.score_rect.center = (100, 20)

    def Resta(self):
        if(self.Puntos > 4):
            self.Puntos = 0