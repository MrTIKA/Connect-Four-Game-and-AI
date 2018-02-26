from game import * 
import random

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)

        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        '''returns a string representing an AIPlayer object'''
        return Player.__repr__(self) + " ("+ self.tiebreak+", "+ str(self.lookahead)+")"


    def max_score_column(self, scores):
        '''takes a list scores containing a score for each column of the board,
           and that returns the index of the column with the maximum score
        '''

        maxS = max(scores)
         
        indexs = [ i for i in range(len(scores)) if scores[i] == maxS]

        if self.tiebreak == 'LEFT' : return indexs[0]
        elif self.tiebreak == 'RIGHT' : return indexs[-1]
        else: return random.choice(indexs)


    def scores_for(self, board):
        '''takes a Board object board and determines the called AIPlayer‘s scores for the columns in board
        '''
        
        scores = [50]*board.width

        for col in range(board.width):
            if not(board.can_add_to(col)): scores[col] = -1
            elif board.is_win_for(self.checker): scores[col] = 100
            elif board.is_win_for(self.opponent_checker()): scores[col] = 0
            elif self.lookahead == 0: scores[col] = 50
            else:
                
                board.add_checker(self.checker, col)
                
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                
                opp_scores = opponent.scores_for(board)
                

                if 0 == max(opp_scores): scores[col] = 100
                
                elif 50 == max(opp_scores): scores[col] = 50
                
                elif 100 == max(opp_scores): scores[col] = 0
                
               
                board.remove_checker(col)

        
        return scores

    def next_move(self, board):
        '''returns the called AIPlayer‘s judgment of its best possible move'''

        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)

















