import pygame
from Scene import Scene
from Enemigo import ENEM
from Puntuacion import Puntuacion

class Fleet:
    def __init__(self, game):
        self.game = game
        self.app = game.app
        self.screen = self.app.screen
        self.Orientacion = 1
        self.ENEMS = []
        self.create_fleet()
        self.score = Puntuacion(self.app)
        
    def create_fleet(self):
        for i in range(30, self.app.width - 100, 120):
            for j in range(30, int(self.app.height/2), 80):
                self.ENEM = ENEM(i, j, self)
                self.ENEMS.append(self.ENEM)
    def draw(self):
        for ENEM in self.ENEMS:
            ENEM.draw()
    def update(self):
        for ENEM in self.ENEMS:
            ENEM.update(self.Orientacion)
            if ENEM.Checar_Bordes():
                self.Orientacion *= -1

            if ENEM.Checar_Borde_INF():
                
                #self.app.change_scene('gameover')
                self.ENEMS.clear()
                print("perdiste")