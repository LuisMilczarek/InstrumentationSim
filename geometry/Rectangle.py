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

    def on_draw(self):
        matrix = self.matrix
        h = self.height/2
        w = self.width/2
        points = [[-w, h],[w, h],
                  [w,-h], [-w,-h]]
        global_points = []
        for x,y in points:
            gx,gy = self.getPointPos(matrix, x,y)
            global_points.append((gx,gy))
        
        pg.draw.polygon(self.screen, self.color, global_points)
        self.drawChilds()
        