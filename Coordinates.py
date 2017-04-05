import Constants

class Coordinates:

    #creates coordinate
    def __init__(self, x, y):
        #From alphabet to integer
        x = ord(x)-65
        y = y-1
        #raises exception x and/or y is outside the game board
        if (x > Constants.MAX_X or x < Constants.MIN_X or y > Constants.MAX_Y or y < Constants.MIN_Y):
            raise InvalidCoordinateException((x,y))
        else:
            self.xcoord = x
            self.ycoord = y

    #returns the x value
    def getX(self):
        return self.xcoord

    #returns the y value
    def getY(self):
        return self.ycoord

#exception class
class InvalidCoordinateException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
