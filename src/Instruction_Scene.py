from Scene import Scene
import pygame

class Instrucciones(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Para activar tu poder, presiona Espacio cuando tengas", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        self.title2 = app.font.render("Mas de 4 puntos, esto los gastara", True, (255,255,255))
        self.title2_rect = self.title2.get_rect()
        self.title2_rect.center = (app.width//2, app.height//2+50)
        self.title3 = app.font.render("todos para usar una bala indetenible.", True, (255,255,255))
        self.title3_rect = self.title2.get_rect()
        self.title3_rect.center = (app.width//2-25, app.height//2+100)
        self.subtitle = app.font.render("Presiona ESC para regresar al inicio", True, (255,255,255))
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.center = (app.width//2, app.height//2+150)
        super().__init__('Instruct') 
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            
    def update(self):
        pass
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.title2, self.title2_rect)
        self.screen.blit(self.title3, self.title3_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)
    def exit(self):
        print('termina: ', self.name)