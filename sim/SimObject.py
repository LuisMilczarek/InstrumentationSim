
import numpy as np
import pygame as pg

from .SimBase import SimBase

class SimObject(SimBase):
    def __init__(self, screen) -> None:     
        super().__init__()   
        self.__pose = np.matrix([0,0,0])
        self.screen = screen

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
    def matrix(self) -> np.matrix:
        matrix = np.matrix([[np.cos(self.pose[0,2]), -np.sin(self.pose[0,2]), self.pose[0,0]],
                             [np.sin(self.pose[0,2]),   np.cos(self.pose[0,2]), self.pose[0,1]],
                                                 [0,                        0,             1]])
        return self.parent.matrix * matrix
    
    def drawChilds(self):
        for child  in self.getChilds():
            child.draw()

    def draw(self):
        raise NotImplementedError