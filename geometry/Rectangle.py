import pygame as pg
from sim import SimObject

class Rectangle(SimObject):
    def __init__(self, screen, height = 1, width = 1) -> None:
        super().__init__(screen)
        self.height = height
        self.width = width
    
    @property
    def height(self) -> float:
        return self.__height
    
    @height.setter
    def height(self, height : float):
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width
    
    @width.setter
    def width(self, width : float):
        self.__width = width

    def draw(self):
        matrix = self.scaleMatrix
        pose = self.global_pose
        # print(matrix)
        
        w, h = self.getPointPos(matrix, self.width, self.height)
        # print(f"W: {w}, h: {h}")
        rec = pg.Rect(pose.x - (w/2), pose.y +( h/2), w, -h)
        pg.draw.rect(self.screen, self.color, rec)
        