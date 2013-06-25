from mojo.events import addObserver
from mojo.roboFont import *

class pointCoordinates:
    
    def __init__(self):
        addObserver(self, 'showCoordinates', 'mouseDown')
        
        c = CurrentGlyph()

        for contour in c:
                    
            for bpoint in contour.bPoints:
                print bpoint.anchor
                print bpoint.bcpIn
                print bpoint.bcpOut
        
    def showCoordinates(self, info):
        # print info
        pass

pointCoordinates()