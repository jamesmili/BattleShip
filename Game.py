from State import *

def main():

    print "Rules for battleship: \n"
    print "1) Each Player gets two boards, and five ships"
    print "2) Objective is to sink all of your opponents ships"
    print "3) Firing shots by typing coordinates 'A', 3"
    print "4) You can only have one length 2 ship, two length 3 ships, one length 4 ship, and one length 5 ship"
    p1 = State("Player1")
    p2 = State("Player2")

    #set up Battleships
    print "Player 1 Setup Battleships\n"
    while p1.shipsavailable != []:
        p1.printShipBoard()
        sx, sy = input("Enter starting coordinate of ship: ")
        ex, ey = input("Enter ending coordinate of ship: ")
        p1ship = Ship(Coordinates(sx, sy), Coordinates(ex, ey))
        p1.setShip(p1ship)

    print "Player 2 Setup Battleships\n"
    while p1.shipsavailable != []:
        p2.printShipBoard()
        sx, sy = input("Enter starting coordinate of ship: ")
        ex, ey = input("Enter ending coordinate of ship: ")
        p2ship = Ship(Coordinates(sx, sy), Coordinates(ex, ey))
        p2.setShip(p2ship)

    #start game
    while True:
        print "Player 1's Turn"
        p1.printP2Board(p2)
        p1mx, p1my = input("Enter firing coordinate (ex. 'A', 3): ")
        p1.fire(Coordinates(p1mx, int(p1my)), p2)
        if p1.isGameOver(p2):
            break
        print "Player 2's Turn"
        p2.printP2Board(p1)
        p2mx, p2my = input("Enter firing coordinate (ex. 'A', 3): ")
        p2.fire(Coordinates(p2mx,int(p2my)), p1)
        if p2.isGameOver(p1):
            break

if __name__ == "__main__":
    main()
