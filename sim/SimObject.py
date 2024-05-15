
import numpy as np
import pygame as pg

from .SimBase import SimBase

from typing import List, Tuple

class SimObject(SimBase):
    def __init__(self, screen) -> None:     
        super().__init__()   
        self.__pose = np.matrix([0,0,0])
        self.screen = screen
        self.__color = pg.Color(255,0,0)
        self.__cachedMatrix = None
        self.__cached = False

    @property
    def pose(self) -> np.matrix:

        return self.__pose
    
    @pose.setter
    def pose(self, pose : np.matrix):
        self.__pose = np.matrix(pose)
    
    @property
    def global_pose(self):
        pose = np.matrix([[0,0,1]])
        globalPose = self.matrix * pose.transpose()
        globalPose = pg.Vector2(globalPose[0], globalPose[1])
        return globalPose
    
    @property
    def color(self) -> pg.color:
        return self.__color
    
    @color.setter
    def color(self, color : pg.Color):
        self.__color = color

    
    @property
    def matrix(self) -> np.matrix:
        if not self.__cached:
            self.__cached = True
            self.__cachedMatrix = self.parent.matrix * np.matrix([[np.cos(self.pose[0,2]),  -np.sin(self.pose[0,2]), self.pose[0,0]],
                                                                  [np.sin(self.pose[0,2]),   np.cos(self.pose[0,2]), self.pose[0,1]],
                                                                  [                     0,                        0,             1]])
        return self.__cachedMatrix
    
    def resetCache(self):
        self.__cachedMatrix = None
        self.__cached = False

    def getPointPos(self, matrix : np.matrix, x : float, y : float) -> "tuple[float,float]":
        result = matrix * np.matrix([[x],[y],[1]])
        return result[0,0], result[1,0]

    
    def drawChilds(self):
        for child  in self.getChilds():
            child.draw()

    def draw(self):
        self.on_draw()        
        self.drawChilds()
        self.resetCache()
    
    def on_draw(self):
        raise NotImplementedError