from Scene import Scene
from ship import Ship
from Puntuacion import Puntuacion
from Fleet import Fleet
import pygame



class Play_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        self.Puntuacion = Puntuacion(app)
        self.Fleet = Fleet(self)
        super().__init__('PlayScene')


    def start(self):
        print('Se inicia: ', self.name)
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
                print("espacio")
                self.ship.DispararESP()
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

    def draw(self):
        self.screen.fill((225, 225, 225))
        #pygame.draw.circle(self.screen, (0, 0, 0), (self.app.width/2, self.app.height/2), 30)
        self.ship.draw()
        self.Puntuacion.draw()
        self.Fleet.draw()

    def exit(self):
        print('Termina: ', self.name)

