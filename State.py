from Ships import *
import Constants

class State:

    def __init__(self, name):
        self.name = name
        self.board = [[" "]*11 for _ in range(9)]
        self.shipBoard = [[" "]*11 for _ in range(9)]
        self.ships = []
        self.shipsavailable = [Constants.ship1length, Constants.ship2length, Constants.ship3length, Constants.ship4length, Constants.ship5length]

    #x,y coordinate of the opposing player's board
    def fire(self,coordinate,p2):
        if self.hit(coordinate,p2) == True and p2.board[coordinate.getY()][coordinate.getX()] == " ":

            p2.board[coordinate.getY()][coordinate.getX()] = "X"
            p2.shipBoard[coordinate.getY()][coordinate.getX()] = "X"

        elif p2.board[coordinate.getY()][coordinate.getX()] == " ":
            p2.board[coordinate.getY()][coordinate.getX()] = "O"
        else:
            raise SameShotException("Shot was taken at a marked coordinate")

    # prints the opponent's board for client
    def printP2Board(self, p2gameBoard):
        print "\n"
        row = 9
        for i in range(8,-1,-1):
            print str(row) + " " + str(p2gameBoard.board[i]).replace(",","")
            row -= 1
        print "    {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
        print "\n"

    def printShipBoard(self):
        print "\n"
        row = 9
        for i in range(8,-1,-1):
            print str(row) + " " + str(self.shipBoard[i]).replace(",","")
            row -= 1
        print "    {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
        print "\n"

    #returns board
    def getBoard(self):
        return self.board

    def getCell(self,coordinate):
        return self.board[coordinate.getY()][coordinate.getX()]

    def getShip(self):
        return self.ships

    def getP2Cell(self,coordinate,p2):
        return p2.shipBoard[coordinate.getY()][coordinate.getX()]

    #visualization of board for client
    def printBoard(self):
        print "\n"
        row = 9
        for i in range(8,-1,-1):
            print str(row) + " " + str(self.board[i]).replace(",","")
            row -= 1
        print "    {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
        print "\n"

    #add ship object to ships in current gameboard
    def setShip(self, ship):
        if self.shipsavailable != []:
            self.shipsavailable.remove(ship.getLength())
            self.ships.append(ship)
            for p in ship.getShipCoord():
                self.shipBoard[p[1]][p[0]] = "S"
        else:
            raise ShipInBoardException("Ship already exists")

    # checks if the player hit the opposing players ship
    def hit(self,coordinate, p2):
        if self.getP2Cell(coordinate,p2) == "S":
            for s in p2.getShip():
                for x,y in s.getShipCoord():
                    if x == coordinate.getX() and y == coordinate.getY():
                        s.shipDamaged([coordinate.getX(),coordinate.getY()])
            return True
        else:
            return False

    #if the ship list is empty then all opposing ships have been destroyed
    def isGameOver(self, p2):
        #checks if each ship sunk and if it's true remove it from ship list
        for s in p2.getShip():
            if s.shipSunk() == True:
                p2.getShip().remove(s)
        # if the opposing ship list is empty then the current player is the winner
        if p2.ships == []:
            print self.name + " is the winner"
            return True
        else:
            return False


class ShipInBoardException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class SameShotException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
