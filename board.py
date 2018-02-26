class Board:

    
    def __init__(self, height, width):
        '''constructs a new Board object by initializing the
           three attributes
        '''
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]




    def  __repr__(self):
        """ Returns a string representation for a Board object.
        """
        
        s = ''         # begin with an empty string

        #add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        s += "-" *( 2*(self.width+1)-1)
        s+= "\n"

        for i in range(self.width):
           s+= " "
           a = str((i % 10))
           s+= a

        return s



    def add_checker(self, checker, col):
        '''accepts two inputs: checker, a one-character string that specifies
           the checker to add to the board.col, an integer that specifies the
           index of the column to which the checkershould be added and that adds
           checker to the appropriate row in column col of the board.
        '''

        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        
        for i in range(self.height-1):
            self.slots[i][col] = ' '

            if self.slots[i+1][col] != ' ':
                self.slots[i][col] = checker

                break
        
            
            self.slots[i+1][col] = checker



    def clear(self):
        '''clears the Board object on which it is called
        '''

        self = self.__init__ (self.height, self.width)



    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        ''' returns True if it is valid to place a checker in the column
           col on the calling Board object
        '''
        if  0 <=  col < self.width:
            if self.slots[0][col] == ' ':
                return True
            else:return False
        else:
            return False


    def is_full(self):
         '''returns True if the called Board object is completely full of
            checkers
         '''

         r = True
         for col in range(self.width):
             r = r and not(self.can_add_to(col))
         return r

        

    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object
        '''
        row = 0
        
        while self.slots[row][col] == ' ':
            if row == self.width-1:
                break
            row += 1
            
        self.slots[row][col] = ' '



    def is_win_for(self, checker):
        '''accepts a parameter checker that is either 'X' or 'O', and returns
           True if there are four consecutive slots containing checker on the board
        '''

        return self.is_horizontal_win(checker) or self.is_vertical_win(checker)\
               or self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker)
    


    ######################################
    ########### Win Checkers #############
    ######################################



    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """

        for row in range(self.height- 3):
            for col in range(self.width):
              
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False

    
    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """

        for row in range(self.height- 3):
            for col in range(self.width - 3):
              
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col+ 1] == checker and \
                   self.slots[row + 2][col+ 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        return False


    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """

        for row in range(self.height):
            for col in range(self.width - 3):


                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
                


        return False


        
