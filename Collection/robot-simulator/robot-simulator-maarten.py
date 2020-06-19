from typing import Tuple

NORTH = (0,1)
EAST = (1,0)
SOUTH = (0,-1)
WEST = (-1,0)
direction = (NORTH, EAST, SOUTH, WEST)

class Robot:
    def __init__(self, bearing=NORTH, x:int=0, y:int=0 ):
        self.bearing = bearing
        self.idx = direction.index(bearing)
        self.coordinates = (x,y) 

    def advance(self) -> None:
        """ Updates the x and y coords according to the bearing """
        update = list(self.coordinates)
        update[0] += self.bearing[0]
        update[1] += self.bearing[1]
        self.coordinates = tuple(update)

    def turn_left(self) -> None:
        """ decrement direction idx and set bearing """
        if self.idx > 0: self.idx -= 1
        else: self.idx = 3
        self.bearing = direction[self.idx]

    def turn_right(self) -> None:
        """ Increment direction idx and set bearing """
        if self.idx < 3: self.idx += 1
        else: self.idx = 0
        self.bearing = direction[self.idx]
    
    def simulate(self, instruction: str) -> None:
        """ Loop through instruction and call appropriate method """
        for c in instruction:
            if c is "A": move = self.advance()
            if c is "L": move = self.turn_left()
            if c is "R": move = self.turn_right()
