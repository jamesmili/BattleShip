from Coordinates import *
from Constants import *

class Ship:
    validL = [Constants.ship1length, Constants.ship2length, Constants.ship3length, Constants.ship4length, Constants.ship5length]

    #constructor
    def __init__(self, startCoord, endCoord, length):
        if self.validLength(length) == False:
            raise InvalidShipException("Ship length error")
        elif self.dist(startCoord, endCoord) != length:
            raise InvalidShipException("Coordinate length doesn't match length. Expected:" + str(length) +". Actual:" + str(self.dist(startCoord, endCoord)))
        else:
            self.start = startCoord
            self.end = endCoord
            self.length = length
            self.shipCoord = []
            self.makeShip()

    # makes ship by its coordinates
    def makeShip(self):
        if self.start.getX() == self.end.getX():
            l = self.least(self.start.getY(), self.end.getY())
            gr = self.greater(self.start.getY(), self.end.getY())
            self.shipCoord = [[self.start.getX(),yi] for yi in range(l, gr+1)]

        elif self.start.getY() == self.start.getY():
            l = self.least(self.start.getX(), self.end.getX())
            gr = self.greater(self.start.getX(), self.end.getX())
            self.shipCoord = [ [xi,self.start.getY()] for xi in range(l, gr+1)]

        else:
            raise InvalidShipException("Ship must be horizontal or vertical")

    # used for exception where the length specified is not the equal to the length between two points
    def dist(self, startCoord, endCoord):
        if startCoord.getX() == startCoord.getX():
            return abs(startCoord.getY() - endCoord.getY())+1
        else:
            return abs(startCoord.getX() - endCoord.getX())+1

    def greater(self, c1, c2):
        if c1 > c2:
            return c1
        else:
            return c2

    def least(self, c1, c2):
        if c1 > c2:
            return c2
        else:
            return c1

    def getShipCoord(self):
        return self.shipCoord

    def getLength(self):
        return self.length

    def validLength(self, l):
        if l in self.validL:
            self.validL.remove(l)
            return True
        else:
            return False

    def shipDamaged(self, coord):
        self.shipCoord.remove(coord)

    def shipSunk(self):
        if self.shipCoord == []:
            return True
        else:
            return False

class InvalidShipException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
