from board import Board
from player import Player
from ai import AIPlayer
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One of them should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure that one is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


def process_move(player, board):
    '''this function will perform all of the steps involved in processing a single
       move by the specified player on the specified board.
    '''
    print(player,"'s turn")
    col = player.next_move(board)
    board.add_checker(player.checker,col)
    
    print()
    print(board)
    print()
    
    if board.is_win_for(player.checker):
        print(player,' wins in',player.num_moves,' moves.')
        print("Congratulations!")
        return True
    
    elif board.is_full():
        print("It's a tie!")
        return True
    
    else:
        return False

class RandomPlayer(Player):
    '''inharits from player'''


    
    def next_move(self, board):
        '''chooses at random from the columns in the specified
           board that are not yet full, and returns the index
           of that randomly selected column
        '''

        avcols = [ col for col in range(board.width) if board.can_add_to(col)]

        col = random.choice(avcols)

        self.num_moves += 1
         
        return col
















        
    






    
    
