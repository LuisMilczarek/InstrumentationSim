from sim import SimObject
from sim.SimBase import SimBase

import pygame as pg

import numpy as np

class Circle(SimObject):
    def __init__(self, screen, radius) -> None:
        super().__init__(screen)
        self.__radius = radius
    
    def on_draw(self):
        r, _ = self.getPointPos(self.scaleMatrix, self.__radius, self.__radius)
        pg.draw.circle(self.screen, self.color, self.global_pose, r)
        self.drawChilds()