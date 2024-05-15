import pygame as pg
from sim import SimObject

class Line(SimObject):
    def __init__(self, screen, width : int = 1) -> None:
        super().__init__(screen)
        self.__p1 = None
        self.__p2 = None
        self.__width = width
    @property
    def width(self) -> int:
        return self.__width
    
    @width.setter
    def width(self, width : int) -> None:
        self.__width = width

    @property
    def P1(self) -> SimObject:
        return self.__p1
    
    @P1.setter
    def P1(self, p1 : SimObject) -> None:
        self.__p1 = p1
    
    @property
    def P2(self) -> SimObject:
        return self.__p2
    
    @P2.setter
    def P2(self, p2 : SimObject) -> None:
        self.__p2 = p2
    
    def draw(self):
        w, _ = self.getPointPos(self.scaleMatrix, self.width, self.width)
        pg.draw.line(self.screen, self.color, self.P1.global_pose, self.P2.global_pose, int(w))
        self.drawChilds()