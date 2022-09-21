'''
Shuyue Gao
CS 5001, 2021 Fall
Homework7 - Connect four
This is a program that is designed to make a connect four game in which
    two players play the game in turn and the first player who get four
    pieces connected in a line(horizontally, vertically, or diagonally) 
    would win the game. We get the winner (or None if nobody won) and print
    out the graph when the game is finished or when the player quitted.
'''


class ConnectFour:
    '''
    Class ConnectFour
    Methods: add_piece, undo, is_game_over, get_winner
    '''
    def __init__(self):
        '''
        Initializes our game to contain the default height, width of the
            board. We initialize the winner to None (nobody), the stack
            to be empty and the queue to contain the marked signs "X" and
            "O" of the two player respectively. We also create the board
            matrix/list with the default height and width.
        '''
        self.height = 6
        self.width = 7
        self.board = [[' ' for x in range(self.width)]
                      for y in range(self.height)]
        self.win = None
        self.stack = []
        self.queue = ["X", "O"]

    def add_piece(self, entered_column):
        '''
        add_piece
        A function that is designed to put the corresponding marked sign 
            (either "X" or "O") in the spot of the board chosen by the
            player to add a piece, depending on which player's turn it is,
            when the spot of the board is valid, is not occupied, or the
            game is not over yet. 
        Parameters: A integer represents the input column 
        Return: Nothing
        except ValueError: If the column is less than 0 or larger than
            or equal to the height, if the columns is already full, or
            if the game is already over
        '''
        if entered_column > self.width - 1 or entered_column < 0:
            raise ValueError("Invalid input for column!")
        if self.is_game_over() is True:
            raise ValueError("The game is over!")
        if self.board[0][entered_column] != " ":
            raise ValueError("The columns are full!")
        # When the spot of the board is not occupied, the elements (["X",
        #   "O"]) in the queue list swich places after the piece is added 
        #   since it is the other player's turn after this player made the 
        #   move. And the stack list should add the corrdinates of the 
        #   picked spot to its list to prepare in case some player wants
        #   to undo a step
        for each_row in range(self.height - 1, -1, -1):
            coordinate = (each_row, entered_column)
            if self.board[each_row][entered_column] == " ":
                player_turn = self.queue.pop(0)
                self.board[each_row][entered_column] = player_turn
                self.queue.append(self.board[each_row][entered_column])
                self.stack.append(coordinate)
                break

    def undo(self):
        '''
        undo
        A function that is designed to let the player to undo the previous 
            step. If undo the steps constantly, it should continue undo 
            steps of both players until there is no step to undo anymore.
        Return: Nothing
        '''
        # To undo the step, we remove the last coordinate that we previously 
        #   put in the stack list and make the spot in the board to be " " 
        #   again. After undo the step, it is still the player's turn to put a
        #   piece in another spot. So the elements in queue list should swich 
        #   places back to before it add piece to board. If the players  
        #   continue the undo steps, the stack should remove the coordinates  
        #   in a first in, last out order until there is no coordinate/element  
        #   to pop and the elements "X" and "O" should continue to switch   
        #   places until the player decide to add another piece again
        if self.stack != []:
            coordinate = self.stack.pop()
            (each_row, each_column) = coordinate
            self.board[each_row][each_column] = " "
            player_turn = self.queue.pop(0)
            self.queue.append(player_turn)
        else:
            raise ValueError("There is no step to undo.")

    def is_game_over(self):
        '''
        is_game_over
        A function that is designed to check whether there are four pieces
            in a line (horizontally, vertically or diagonally) for a player 
            either using "X" or "O" and find out the winner of the game. 
        Return: Boolean results. The function returns true when four pieces
            is in a line (horizontally, vertically or diagonally) and a winner 
            has been generated. If there is no winner (there is no spot left
            in the board), the function should return false.
        '''
        # Check vertical for columns
        for each_row in range(self.height - 3):
            for each_column in range(self.width):
                if self.board[each_row][each_column] != " " and \
                   self.board[each_row][each_column] == \
                   self.board[each_row + 1][each_column] == \
                   self.board[each_row + 2][each_column] == \
                   self.board[each_row + 3][each_column]:
                    self.win = self.board[each_row][each_column]
                    return True
        # Check horizontal for rows
        for each_row in range(self.height):
            for each_column in range(self.width - 3):
                if self.board[each_row][each_column] != " " and \
                   self.board[each_row][each_column + 1] == \
                   self.board[each_row][each_column + 2] == \
                   self.board[each_row][each_column + 3] == \
                   self.board[each_row][each_column]:
                    self.win = self.board[each_row][each_column]
                    return True
        # Check top right to bottom left diagonals
        for each_row in range(self.height - 3):
            for each_column in range(self.width - 4, self.width):
                if self.board[each_row][each_column] != " " and \
                   self.board[each_row][each_column] == \
                   self.board[each_row + 1][each_column - 1] == \
                   self.board[each_row + 2][each_column - 2] == \
                   self.board[each_row + 3][each_column - 3]:
                    self.win = self.board[each_row][each_column]
                    return True
        # Check top left to bottom right diagonals
        for each_row in range(self.height - 3):
            for each_column in range(self.width - 3):
                if self.board[each_row][each_column] != " " and \
                   self.board[each_row][
                       each_column] == \
                   self.board[each_row + 1][each_column + 1] == \
                   self.board[each_row + 2][each_column + 2] == \
                   self.board[each_row + 3][each_column + 3]:
                    self.win = self.board[each_row][each_column]
                    return True
        return False

    def get_winner(self):
        '''
        get_winner
        A function that is designed to check whether there is a winner for
            the game. 
        Return: If there is a winner, get the winning player who used either
        "X" or "O". If there is no winner, returns None.
        '''
        # If self.is_game_over() is False, there is no winner. If the previous
        #   function returned True, there is a winner.
        if self.is_game_over() is False:
            return None
        else:
            return self.win

    def __str__(self):
        '''
        A function returns a string representing the game object (the
            returned contents in the function can be printed when a class
            object is defined)
        Returns: a string that represents the expected to print contents of
            the game object
        '''
        graph = ""
        for each_row in range(self.height):
            for each_column in range(self.width):
                graph += "|" + self.board[each_row][each_column]
            graph += "|\n"
            graph += 15 * "-" + "\n"
        return graph
