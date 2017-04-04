import Constants

class Coordinates:

    def __init__(self, x, y):
        x = ord(x)-65
        y = y-1
        if (x > Constants.MAX_X or x < Constants.MIN_X or y > Constants.MAX_Y or y < Constants.MIN_Y):
            raise InvalidPointException((x,y))
        else:
            self.xcoord = x
            self.ycoord = y

    def getX(self):
        return self.xcoord

    def getY(self):
        return self.ycoord


class InvalidPointException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
