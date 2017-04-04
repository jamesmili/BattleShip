from Ships import *

class GameState:
    #create board
    def __init__(self, name):
        self.name = name
        self.board = [[" "]*11 for _ in range(9)]
        self.shipBoard = [[" "]*11 for _ in range(9)]
        self.ships = []

    #x,y coordinate of the opposing player's board
    def fire(self,coordinate,p2):
        if self.hit(coordinate,p2) == True and p2.board[coordinate.getY()][coordinate.getX()] == " ":

            p2.board[coordinate.getY()][coordinate.getX()] = "X"
            self.shipBoard[coordinate.getY()][coordinate.getX()] = "X"

        else:
            p2.board[coordinate.getY()][coordinate.getX()] = "O"

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
        return self.board[coordinate.getX()][coordinate.getY()]

    def getShip(self):
        return self.ships

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
    def putShip(self, ship):
        self.ships.append(ship)
        for p in ship.getShipCoord():
            self.shipBoard[p[1]][p[0]] = "S"

    # checks if the player hit the opposing players ship
    def hit(self,coordinate, p2GameState):
        for s in p2GameState.getShip():
            if s.shipSunk() != True:
                for x,y in s.getShipCoord():
                    if coordinate.getX() == x and coordinate.getY() == y:
                        return True
        return False

    def isGameOver(self, p2GameState):
        if p2GameState.ships == []:
            print self.name + " is the winner"
            return True
        else:
            return False


class ShipInBoardException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
