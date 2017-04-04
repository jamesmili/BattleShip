from GameState import *

def main():

    print "Rules for battleship: \n"
    print "1) Each Player gets two boards, and five ships"
    print "2) Objective is to sink all of your opponents ships"
    print "3) Firing shots by typing coordinates 'A', 3"
    print "4) You can only have one length 2 ship, two length 3 ships, one length 4 ship, and one length 5 ship"
    p1 = GameState("Player1")
    p2 = GameState("Player2")

    #set up Battleships
    print "Player 1 Setup Battleships\n"
    for i in range(4):
        p1.printShipBoard()
        sx, sy = input("Enter starting coordinate of ship: ")
        ex, ey = input("Enter ending coordinate of ship: ")
        length = input("Enter length of ship (2-4): ")
        p1ship = Ship(Coordinates(sx, sy), Coordinates(ex, ey), length)
        p1.putShip(p1ship)

    print "Player 2 Setup Battleships\n"
    for i in range(4):
        p2.printShipBoard()
        sx, sy = input("Enter starting coordinate of ship: ")
        ex, ey = input("Enter ending coordinate of ship: ")
        length = input("Enter length of ship (2-4)")
        p2ship = Ship(Coordinates(sx, sy), Coordinates(ex, ey), length)
        p2.putShip(p2ship)

    while p1.isGameOver() != False or p2.isGameOver() != False:
        p1.printP2Board()
        p1move = input("Enter firing coordinate (ex. 'A', 3): ")
        p1.shot(Coordinates(p1move), p2)
        p2.printP2Board()
        p2move = input("Enter firing coordinate (ex. 'A', 3): ")
        p2.shot(Coordinates(p2move), p1)



if __name__ == "__main__":
    main()
