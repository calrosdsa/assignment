from dataclasses import dataclass,field
from typing import ClassVar

@dataclass
class ChessProblemEntity:
    n:int = None
    k:int = None
    rq:int = None
    cq:int = None
    obstacles:list[list[int]] =  field(default_factory=list)
    
    
    def queensAttack(self) -> int:
        # Calculate the number of squares available in each direction before encountering the edge of the board
        top = self.n - self.rq 
        left = self.cq - 1     
        right = self.n - self.cq 
        bottom = self.rq - 1    

        # Calculate the number of squares available in each diagonal direction before encountering the edge of the board
        top_left = min(top, left)         
        top_right = min(top, right)       
        bottom_left = min(bottom, left)   
        bottom_right = min(bottom, right) 

        # Loop through each obstacle
        for i in range(self.k):
            r_o, c_o = self.obstacles[i][0], self.obstacles[i][1]  # Get the row and column of the obstacle
            
            # Check if the obstacle is in the same row as the queen
            if r_o == self.rq:
                if c_o > self.cq:  
                    right = min(right, c_o - self.cq - 1)
                else:  
                    left = min(left, self.cq - c_o - 1)

            # Check if the obstacle is in the same column as the queen
            if c_o == self.cq:
                if r_o > self.rq:  
                    top = min(top, r_o - self.rq - 1)
                else:  
                    bottom = min(bottom, self.rq - r_o - 1)

            # Check if the obstacle is on the same diagonal as the queen
            if abs(c_o - self.cq) == abs(r_o - self.rq):
                if c_o > self.cq and r_o > self.rq:  
                    top_right = min(top_right, c_o - self.cq - 1)
                if c_o > self.cq and r_o < self.rq:  
                    bottom_right = min(bottom_right, c_o - self.cq - 1)
                if c_o < self.cq and r_o > self.rq:  
                    top_left = min(top_left, self.cq - c_o - 1)
                if c_o < self.cq and r_o < self.rq:  
                    bottom_left = min(bottom_left, self.cq - c_o - 1)

        # Sum up all the available squares in all directions
        return right + left + top + bottom + bottom_left + top_left + bottom_right + top_right

