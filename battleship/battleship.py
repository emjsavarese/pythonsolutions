"""
File: battleship.py
Author: Emily Savarese
Purpose: plays one half of a battleship game; creates a board based on given placements and
guesses the board using given guesses
CSC 120, Section 1C, Fall 2018
"""

import sys

class GridPos:
    """creates a gridpos in the grid"""
    def __init__(self,x,y):
        """Parameters: x is the x position on the grid, y is the y position.
        ship indicates whether or not there's a ship in this position.
        guess is whether or not this position has been guessed."""
        self._x=x
        self._y=y
        self._ship=None
        self._guess=False

    def guessed(self):
        #happens when this gridpos is guessed
        self._guess=True

    def guess(self):
        return self._guess

    def ship (self):
        return self._ship

    def add_ship(self,ship):
        #assigns a ship to the ship attribute
        self._ship=ship

    def __str__(self):
        return (str(self._x) + "," + str(self._y)+ " "+  str(self._ship))




class Board:
    """creates a board of gridposes"""
    def __init__(self,grid):
        """grid is the list of lists of gridpos objects.
        ships is a dict containing the names and sizes of correct ships.
        shipsact is a list of ship objects that the placement file makes."""
        self._grid=grid
        self._ships= {"A":5 ,"B":4,"S":3, "D":3, "P":2}
        self._shipact=[]

    def newship(self,ship):
        self._shipact.append(ship)

    def shipact(self):
        return self._shipact

    def ships(self):
        return self._ships

    def alldone(self):
        #checks to see if every ship in shipact is sunk.
        for i in range(len(self._shipact)):
            if not self._shipact[i].check_sunk():
                return False
        return True

    def grid(self):
        return self._grid

    def __str__(self):
        newgrid=[]
        for i in range(len(self._grid)):
            newline=[]
            for j in range(len(self._grid[i])):
                newline.append(str(self._grid[i][j]))
            newgrid.append(newline)
        return (str(newgrid))
                
        
    

class Ship:
    """creates a ship"""
    def __init__(self,kind,size):
        """kind is the kind of ship it is (A,B, etc).
        size is the length of the ship.
        poses is the positions where the ship is placed.
        nothit contains the ships that have not been hit.
        sunk reveals whether or not a ship is sunk"""
        self._kind=kind
        self._size=size
        self._poses=[]
        self._nothit=[]
        self._sunk=False

    def kind(self):
        return self._kind
    
    def size(self):
        return self._size

    def add_pos(self,poses):
        self._poses=poses
        self._nothit=poses
    
    def check_sunk(self):
        #checks to see if every position in poses has been guessed
        for i in range(len(self._poses)):
            if not self._poses[i].guess():
                return self._sunk
        self._sunk = True
        return self._sunk

    def __str__(self):
        return self._kind + ":" + str(self._size)


        

def read_placements(board):
    """creates ships and assigns them to their proper positions on the board.
    board is the Board object composed of gridPos objects."""
    try:
        file=input()
        file=open(file)
    except:
        #errors out if file not found
        print("ERROR: Could not open file: " + file)
        sys.exit(1)
    file=file.readlines()
    for i in range(len(file)):
        shipstats=file[i].strip().split()
        check_pos(shipstats, file[i])
        kind=shipstats[0]
        
        p1=(int(shipstats[1]), int(shipstats[2]))
        p2=(int(shipstats[3]), int(shipstats[4]))
        ordered=sorted([p1,p2])          #puts them in order so they can loop correctly
        size=generate_size(ordered,file[i],board,kind)
        
        ship=Ship(kind,size)
        poses=get_positions(ordered[0][0],ordered[0][1],ordered[1][0],ordered[1][1],board,file[i],ship)
        ship.add_pos(poses)
        board.newship(ship)
        
    check_ships(board)



def check_ships (board):
    """checks the composition of the completed board.shipact list
    to what it should actually look like. Errors out if False.
    board is the list of lists of gridpos objects."""
    real_ships=["A", "B", "D", "P", "S"]
    shipnames=[]
    for i in range(len(board.shipact())):
        shipnames.append(board.shipact()[i].kind())
    if sorted(shipnames) != real_ships:
        print ("ERROR: fleet composition incorrect")
        sys.exit(1)



  

def generate_size(ordered,line,board,kind):
    """generates the size of the ship.
    ordered is an ordered list of positions (x1,y1)(x2,y2)
    board is the list of lists of gripos objects.
    kind is the kind of ship.
    returns the size of the ship."""
    ships_sizes=board.ships()
    if (ordered[0][0]!= ordered [1][0]) and (ordered[0][1] != ordered[1][1]):
        print("ERROR: ship not horizontal or vertical: " + line)
        sys.exit(1)
    if ordered[0][0]==ordered[1][0]:
        size=int(ordered[1][1])-int(ordered[0][1]) +1
    else:
        size=int(ordered[1][0])-int(ordered[0][0]) +1
    if int(ships_sizes[kind]) != int(size):
        print ("ERROR: incorrect ship size: " + line) #errors out if the kind of ship does not match size
        sys.exit(1)
    
    return size



def get_positions(x1,y1,x2,y2,board,errorm,ship):
    """x1 is the first x position.
    y1 is the first y position.
    x2 is the second x position.
    y2 is the second y position.
    errorm is the line that caused an overlapping ship.
    ship is the current ship.
    returns positions for a given ship."""
    poses=[]
    grid=board.grid()
    for i in range(y1, y2+1):
        for j in range(x1,x2+1):
            poses.append(grid[i][j])
            if grid[i][j].ship() != None:
                print ("ERROR: overlapping ship: " + errorm)
                sys.exit(1)
            grid[i][j].add_ship(ship)
    return poses
            

        
def create_grid():
    """creates a grid (list of lists) of gridpos objects.
    returns a grid."""
    grid=[]
    for i in range(10):
        line=[]
        for j in range(10):
            pos=GridPos(j,i)
            line.append(pos)
        grid.append(line)
    return grid


def check_pos(lis, line):
    """checks to see if a ship's coordinates are out of bounds.
    lis is the list of positions.
    line is the line where the coordinates were out of bounds."""
    for i in range(1, len(lis)):
        if (int(lis[i]) >9) or (int(lis[i]) <0):
            print ("ERROR: ship out-of-bounds: " + line)
            sys.exit(1)


def read_guess(board):
    """analyzes the input guesses.
    returns the victory message if all ships are sunk.
    returns None otherwise.""" 
    try:
        file=input()
        file=open(file)
    except:
        print("ERROR: Could not open file: " + file)
        sys.exit(1)
    i=0
    file=file.readlines()
    for i in range(len(file)):
        guess=file[i].strip().split()
        if check_guess(guess):   #checks legality of guess
            print("illegal guess")
            
        else:
            fullguess=board.grid()[int(guess[1])][int(guess[0])]
            if fullguess.ship()==None: #No ship in this gridpos
                if not fullguess.guess(): #if the gridpos has not been guessed, make it guessed
                    fullguess.guessed()
                    print("miss")
                else:
                    print("miss (again)") #if gridpos has been guessed
                    
            if fullguess.ship()!=None: #gripos has a ship
                ship=fullguess.ship()
                if not fullguess.guess():
                    fullguess.guessed() #if not guessed, make it guessed and check if it sunk
                    if ship.check_sunk():
                        print(ship.kind() + " sunk")
                    else:
                        print ("hit")
                else:
                    print("hit (again)")
                    
        if board.alldone(): #if all ships are sunk
            return "all ships sunk: game over"
   
    
def check_guess(guess):
    """checks to see if the guess is legal.
    guess is an x and y position.
    returns whether or not its legal."""
    for i in range(len(guess)):
        if (int(guess[i]) >9) or (int(guess[i]) <0):
            return True
    return False



def main():
    grid=create_grid()
    board=Board(grid)
    read_placements(board)
    mssg=read_guess(board)
    if mssg!= None:
        print(mssg)



main()


    
