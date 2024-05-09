import numpy as np

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
        self.__childs.append(child)

    def getChilds(self) -> "SimBase":
        return self.__childs
    
    def drawChilds(self):
        for child  in self.getChilds():
            child.draw()
    
    @property
    def matrix(self) -> np.matrix:
        raise NotImplementedError