from Scene import Scene
import pygame



class Intro_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Invaders", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        self.letters = app.font.render("Presiona Enter para iniciar", True, (255,255,255))
        self.letters_rect = self.letters.get_rect()
        self.letters_rect.center = (app.width//2, app.height//2 + 200)
        super().__init__('IntroScene') 
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('play')
                print('se presiono una tecla')
            
    def update(self):
        pass
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.letters, self.letters_rect)
    def exit(self):
        print('termina: ', self.name)

