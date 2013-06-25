from mojo.events import addObserver
from mojo.roboFont import *
from mojo.drawingTools import *
import math

class pointCoordinates(object):
    
    def __init__(self):
        addObserver(self, 'output', 'draw')
        #addObserver(self, 'output', 'keyUp')

    def output(self, info):

        scale = info["scale"]
           
        c = CurrentGlyph()

        for contour in c:
            #print '--------'   
            listOfAllPoints = contour.points
            onCurvePoints = self.returnOnCurvePoints(listOfAllPoints)
            bPoints = contour.bPoints

            i = 0
            for point in onCurvePoints:
                pointIndex = onCurvePoints.index(point)
                bpoint = bPoints[pointIndex]
                if point.selected:
                    anchor = bpoint.anchor
                    h_in = bpoint.bcpIn
                    h_out = bpoint.bcpOut
                    # self.printCoordinates(h_in, anchor, h_out)
                    fill(0, 0, 0)
                    stroke(0)
                    fontSize(25/scale)
                    text(self.printDistances(h_in, anchor, h_out), (0, i))
                    i -= 40/scale 
                    
    
        

    def returnOnCurvePoints(self, list):
        onCurvePoints = []
        for point in list:
            if point.type is not 'offCurve':
                onCurvePoints.append(point)
        
        return onCurvePoints

    def printCoordinates(self, h_in, anchor, h_out):

        h_in_str, anchor_str, h_out_str = self.createStrings(h_in, anchor, h_out)
        print '%s[%s]%s' % (h_in_str, anchor_str, h_out_str)

    def printDistances(self, h_in, anchor, h_out):
        dist_in = round(math.hypot(0 - h_in[0], 0 - h_in[1]), 2)
        dist_out = round(math.hypot(0 - h_out[0], 0 - h_out[1]), 2)
        
        h_in_coord = (anchor[0] + h_in[0], anchor[1] + h_in[1])
        h_out_coord = (anchor[0] + h_out[0], anchor[1] + h_out[1])

        slope, intercept = calcSlopeAndIntersect(h_in_coord, h_out_coord)
        anchorType = isPointOnLine(slope, intercept, anchor)

        if dist_in != 0.0:
            dist_in_str = '\t' + str(dist_in) + '\t'
        else:
            dist_in_str = '\t'


        if dist_out != 0.0:
            dist_out_str = '\t' + str(dist_out) + '\t'
        else:
            dist_out_str = ''

        return str(anchor) + '\t%s(%s)%s' % (dist_in_str, anchorType, dist_out_str)

    def createStrings(self, h_in, anchor, h_out):
        if str(h_in) != '(0, 0)':
            h_in = str((anchor[0] + h_in[0], anchor[1] + h_in[1])) + '----'
        else:
            h_in = ''

        if str(h_out) != '(0, 0)':
            h_out = '----' + str((anchor[0] + h_out[0], anchor[1] + h_out[1]))
        else:
            h_out = ''

        anchor = str(anchor)

        return h_in, anchor, h_out

def calcSlopeAndIntersect(point1, point2):
    try:
        slope = (point1[1]+ 0.0 - point2[1]) / (point1[0] + 0.0 - point2[0])
        intercept = point1[1] - (slope * point1[0])
    except ZeroDivisionError:
        slope = 0
        intercept = 0
    return slope, intercept

def isPointOnLine(slope, intercept, pointToCheck):
    if slope != 0 and intercept != 0:
        if pointToCheck[1] - (slope * pointToCheck[0] + intercept) < 0.3:
            return '-'
        else:
            return '^'
    else:
        return '^'

pointCoordinates()