#!/usr/bin/env python

import pygame as pg
import numpy as np
from time import perf_counter

from sim import SimBase, DummyObject
from utils import Rate

from geometry import Circle, Rectangle, Line

class App(SimBase):
    def __init__(self) -> None:
        super().__init__()
        self.__running = True
        self.__display_surf = None
        self.size = self.width, self.height = 1920,1080
        scale = self.width/10
        self.scaleMatrix = self.createScaleMatrix(scale, -scale)
        self.translationMatrix = self.createTranslationMatrix(self.width/2, self.height/2)
        self.pause = False

    @property
    def matrix(self):
        return self.scaleMatrix + self.translationMatrix

    def on_init(self):
        pg.init()
        self.__display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.__running = True
        for i in range(-5,6):
            for j in range(-5,6):
                point = Circle(self.__display_surf,0.025)
                point.pose = np.matrix([i,j,0])
                self.addChild(point)
        self.center = Circle(self.__display_surf, .1)
        self.circle = Circle(self.__display_surf, .1)
        # self.center = DummyObject(self.__display_surf)
        # self.circle = DummyObject(self.__display_surf)
        self.rec = Rectangle(self.__display_surf, 0.5,0.5)
        self.rec.color = pg.Color(0,255,0,)

        self.line = Line(self.__display_surf,.1)
        self.line.color = pg.Color(0,0,0)
        self.line.P1 = self.center
        self.line.P2 = self.circle

        self.line2 = Line(self.__display_surf,.1)
        self.line2.color = pg.Color(0,0,0)
        self.line2.P1 = self.circle
        self.line2.P2 = self.rec

        self.addChild(self.center)
        self.center.addChild(self.circle)
        self.circle.addChild(self.rec)
        self.addChild(self.line)
        self.addChild(self.line2)

        self._initTime = perf_counter()

    def events(self, event):
        if event.type == pg.QUIT:
            self.__running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.pause = not self.pause
                

    def render(self):
        self.__display_surf.fill((255,255,255))
        self.drawChilds()
        pg.display.update()
    
    def pool(self):
        dt = perf_counter() - self._initTime
        # dt *= 0.05
        px = np.cos(np.pi*dt)*2
        py = np.sin(np.pi*dt)*2

        self.circle.pose = np.matrix([px,py,2*np.pi*dt])
        self.rec.pose = np.matrix([1,0,0])
        

    def cleanUp(self):
        pg.quit()

    def run(self):
        if self.on_init() == False:
            self._running = False

        r = Rate(60)
        while self.__running:
            for event in pg.event.get():
                self.events(event)
            if not self.pause:
                self.pool()
            self.render()
            for child in self.getChilds():
                child.resetCache()
            r.sleep()
        self.cleanUp()

if __name__ == "__main__":
    
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        pass