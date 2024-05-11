import numpy as np

from multipledispatch import dispatch
# from typing import overload


class SimBase(object):
    def __init__(self) -> None:
        self.__childs = []
        self.__parent = None
     
    @property
    def parent(self) -> "SimBase":
        return self.__parent
    
    @parent.setter
    def parent(self, parent : "SimBase"):
        self.__parent = parent

    def addChild(self, child : "SimBase"):
        child.parent = self
        child.scaleMatrix = self.scaleMatrix
        self.__childs.append(child)

    def getChilds(self) -> "SimBase":
        return self.__childs
    
    def drawChilds(self):
        for child  in self.getChilds():
            child.draw()
    
    @property
    def matrix(self) -> np.matrix:
        raise NotImplementedError
    
    def createScaleMatrix(self, sx : float, sy : float) -> np.matrix:
        scaleMatrix = np.matrix([[sx,  0, 0],
                                 [ 0, sy, 0],
                                 [ 0,  0,  1]])
        return scaleMatrix
    
    def createTranslationMatrix(self, tx: float, ty : float) -> np.matrix:
        translateMatrix = np.matrix([[0, 0, tx],
                                     [0, 0, ty],
                                     [0, 0,  1]])
        return translateMatrix
    
    @property
    def scaleMatrix(self) -> np.matrix:
        return self.__scaleMatrix
    
    @scaleMatrix.setter
    def scaleMatrix(self, matrix : np.matrix) -> None:
        self.__scaleMatrix = matrix

    @property
    def translationMatrix(self) -> np.matrix:
        return self.__translationMatrix
    
    @translationMatrix.setter
    def translationMatrix(self, matrix : np.matrix) -> None:
        self.__translationMatrix = matrix