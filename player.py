
from board import Board

# Write your Player class below.

class Player:
    
    def __init__(self, checker):
        '''initilizes player class with the given checker
        '''

        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0

    def  __repr__(self):
        '''returns the reprezentation of the Player object
        '''

        return 'Player ' + self.checker

    def opponent_checker(self):
        '''returns a one-character string representing the
           checker of the Player object’s opponent
        '''
        
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, board):
         '''returns the column where the player wants to make
            the next move
         '''
         col = int(input("Enter a column: " ))

         while not(board.can_add_to(col)):
             
             print("Try again!")
             
             col = int(input("Enter a column: " ))

             
         self.num_moves += 1
         
         return col
