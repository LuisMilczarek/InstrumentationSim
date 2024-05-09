from sim import SimObject
from sim.SimBase import SimBase

import pygame as pg

import numpy as np

class Circle(SimObject):
    def __init__(self, screen, radius) -> None:
        super().__init__(screen)
        self.__radius = radius
    
    def draw(self):
        # pose = self.pose[0]
        # pose[0,2] = 1     
        # globalPose = self.parent().matrix * pose.transpose()
        # pose = np.matrix([[0,0,1]])
        # globalPose = self.matrix * pose.transpose()
        # globalPose = pg.Vector2(globalPose[0], globalPose[1])
        self.drawChilds()
        pg.draw.circle(self.screen, "red", self.global_pose, self.__radius)