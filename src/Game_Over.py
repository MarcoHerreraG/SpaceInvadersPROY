from Scene import Scene
import pygame

class Game_Over(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Perdiste", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        self.subtitle = app.font.render("Presiona R para reiniciar", True, (255,255,255))
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.center = (app.width//2, app.height//2+200)
        super().__init__('GameOver') 
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.app.change_scene('play')
                print('se presiono una tecla')
            
    def update(self):
        pass
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)
    def exit(self):
        print('termina: ', self.name)