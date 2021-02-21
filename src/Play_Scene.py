from Scene import Scene
from ship import Ship
from Puntuacion import Puntuacion
from BalasNORM import Bullet
from BalasESP import BalaESP
from Fleet import Fleet
import pygame



class Play_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        self.Puntuacion = Puntuacion(app)
        self.Fleet = Fleet(self)
        self.Muerto = pygame.mixer.Sound("Assets/Audio/Muerto.wav")
        self.Fondo = pygame.image.load("Assets/Image/Space.png")
        super().__init__('PlayScene')


    def start(self):
        print('Se inicia: ', self.name)
        if not self.Fleet.ENEMS:
            self.Fleet.create_fleet()

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pass
            elif event.key == pygame.K_a:
                self.ship.move_left = True
            elif event.key == pygame.K_d:
                self.ship.move_right = True
            elif event.key == pygame.K_SPACE:
                self.ship.DispararESP(self.Puntuacion.Puntos)
                self.Puntuacion.Resta()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.ship.move_left = False
            elif event.key == pygame.K_d:
                self.ship.move_right = False
        if event.type == pygame.MOUSEBUTTONUP:
            self.ship.Disparar()

    def update(self):
        self.ship.update()
        self.Puntuacion.update()
        self.Fleet.update()
        self.collisions()

    def collisions(self):
        for Bullet in self.ship.Weapon.Balas:
            for ENEM in self.Fleet.ENEMS:
                if Bullet.active == True:
                    if(Bullet.rect.x < ENEM.x + ENEM.rect.width and Bullet.rect.x + Bullet.rect.width > ENEM.rect.x and
                    Bullet.rect.y < ENEM.rect.y + ENEM.rect.height and Bullet.rect.y + Bullet.rect.height> ENEM.rect.y):
                        pygame.mixer.Sound.play(self.Muerto)
                        Bullet.active = False
                        self.Fleet.ENEMS.remove(ENEM)
                        self.Puntuacion.Puntos += 1
        
        for BalaESP in self.ship.Weapon.Balas2:
            for ENEM in self.Fleet.ENEMS:
                if BalaESP.active == True:
                    if(BalaESP.rect.x < ENEM.x + ENEM.rect.width and BalaESP.rect.x + BalaESP.rect.width > ENEM.rect.x and
                    BalaESP.rect.y < ENEM.rect.y + ENEM.rect.height and BalaESP.rect.y + BalaESP.rect.height> ENEM.rect.y):
                        pygame.mixer.Sound.play(self.Muerto)
                        self.Fleet.ENEMS.remove(ENEM)
                        self.Puntuacion.Puntos += 1
        if not self.Fleet.ENEMS:
            self.Fleet.create_fleet()

    def draw(self):
        self.screen.blit(self.Fondo, (0, 0))
        #pygame.draw.circle(self.screen, (0, 0, 0), (self.app.width/2, self.app.height/2), 30)
        self.ship.draw()
        self.Puntuacion.draw()
        self.Fleet.draw()

    def exit(self):
        print('Termina: ', self.name)

