#!/usr/bin/env python

import pygame as pg
import numpy as np
from time import perf_counter

from sim import SimObject, SimBase
from utils import Rate

from geometry import Circle

class App(SimBase):
    def __init__(self) -> None:
        super().__init__()
        self.__running = True
        self.__display_surf = None
        self.size = self.width, self.height = 1024,1024
        self.__matrix = np.matrix([[self.width/10,                0,     self.width/2],
                                   [             0, -self.height/10,    self.height/2],
                                   [             0,               0,                1]])


    @property
    def matrix(self):
        return self.__matrix

    def on_init(self):
        pg.init()
        self.__display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.__running = True
        for i in range(-5,6):
            for j in range(-5,6):
                point = Circle(self.__display_surf,2)
                point.pose = np.matrix([i,j,0])
                self.addChild(point)
        self.center = Circle(self.__display_surf, 10)
        self.addChild(self.center)
        self.circle = Circle(self.__display_surf, 10)
        self.addChild(self.circle)
        self.circle2 = Circle(self.__display_surf, 10)
        self.circle.addChild(self.circle2)        

        self._initTime = perf_counter()

    def events(self, event):
        if event.type == pg.QUIT:
            self.__running = False

    def render(self):
        self.__display_surf.fill((255,255,255))
        # for point in self.points:
        #     point.draw()
        # self.center.draw()
        # self.circle.draw()
        # self.circle2.draw()
        self.drawChilds()
        pg.display.update()
    
    def pool(self):
        dt = perf_counter() - self._initTime
        # dt *= 0.05
        px = np.cos(np.pi*dt)*2
        py = np.sin(np.pi*dt)*2

        px2 = np.cos(2*np.pi*dt)
        py2 = np.sin(2*np.pi*dt)

        self.circle.pose = np.matrix([px,py,0])
        self.circle2.pose = np.matrix([px2,py2,0])
        

    def cleanUp(self):
        pg.quit()

    def run(self):
        if self.on_init() == False:
            self._running = False

        r = Rate(60)
        while self.__running:
            for event in pg.event.get():
                self.events(event)
            self.pool()
            self.render()
            r.sleep()
        





if __name__ == "__main__":
    
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        pass