'''
Shuyue Gao
CS 5001, 2021 Fall
Homework7 - Test Connect four
This is a program that is designed to test whether all functions work
    properly in connect_four.py
'''
import connect_four as c
import unittest
import random


class ConnectTest(unittest.TestCase):
    def test_init(self):
        '''
        test_init
       A function that is designed to test whether the initial
           board we created in the __init__ function is an empty
           board of the same size (same height and width)
        Returns: Nothing
        '''
        game = c.ConnectFour()
        actual_board = game.board
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(actual_board, expected_board)

    def test_add_piece_invalid_column(self):
        '''
        test_add_piece_invalid_column
       A function that is designed to test whether it will raise an
            error when the column to put in add_piece function is
            negative or larger than or equal to the width
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # When column is less than 0
        for test in range(5000):
            column_one = -test - 1
            try:
                actual_column = game.add_piece(column_one)
                self.fail("Negative input should have raised an error")
            except ValueError:
                pass
        # When column is larger than or equal to width
        for test in range(5000):
            column_two = test + game.width
            try:
                actual_column = game.add_piece(column_two)
                self.fail("larger than or equal to width input should \
have raised an error")
            except ValueError:
                pass

    def test_add_piece_full_column(self):
        '''
        test_add_piece_full_column
        A function that is designed to test whether it will raise an
            error when the column is full and another column is added
            to the board
        '''
        game = c.ConnectFour()
        # The entire board is filled with "M" so the board is full
        for each_row in range(game.height):
            for each_column in range(game.width):
                game.board[each_row][each_column] = "M"
            # When column is vaild in the board, we should determine
            #   whether another column can still be added to the board
            for test_column in range(game.width):
                try:
                    game.add_piece(test_column)
                    self.fail("column full should've raised an error")
                except ValueError:
                    pass

    def test_add_piece_game_over_column(self):
        '''
        test_add_piece_game_over_column
        A function that is designed to test whether it will raise an
            error when the game is over and another column is added
            to the board
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # When "X" won and the game is over
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'X', ' ', ' ', ' ', ' '],
                      [' ', 'O', 'X', 'X', ' ', ' ', ' '],
                      [' ', 'O', 'O', 'O', 'X', ' ', ' '],
                      [' ', 'O', 'X', 'X', 'O', 'X', ' ']]
        # When column is vaild in the board, we should determine
        #   whether another column can still be added to the board
        for test_column in range(game.width):
            try:
                game.add_piece(test_column)
                self.fail("game over column should've raised an error")
            except ValueError:
                pass

    def test_add_piece(self):
        '''
        test_add_piece
        A function that is designed to test whether columns filled with
            "X" or "O" in turn without a winner can match no winner of
            game with every spot full in the board using the test_add_piece
            function in connect_four.py
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # We fill out the columns and we make a new board every time
        #   we start a new column to test all columns and make sure
        #   there is no winner in the game 
        for column in range(game.width):
            test_game = c.ConnectFour()
            for test in range(game.width - 1):
                try:
                    test_game.add_piece(column)
                except ValueError:
                    self.fail("add piece function raised an error \
on good input.")  

    def test_undo(self):
        '''
        test_add_piece
        A function that is designed to test whether before add board and
            after undo board is the same after using undo function in
            connect_four.py
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # Undo the previous step
        column = random.randint(0, game.width - 1)
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                      [' ', 'X', ' ', 'X', 'O', ' ', 'O']]
        before_add_board = game.board
        try:
            game.add_piece(column)
            game.undo()
            after_undo_board = game.board
        except ValueError:
            self.fail("undo function raised an error on good input.")
        self.assertEqual(before_add_board, after_undo_board)
        # Undo several steps
        game_two = c.ConnectFour()
        game_two.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', 'X', 'X', ' ', 'O', ' '],
                          [' ', 'X', 'O', 'X', 'O', 'O', ' ']]
        before_add_board = game_two.board
        try:
            # We add several spots to the board and then we undo the
            #   previous steps for the same number of times
            for column in range(game_two.width - 1):
                game_two.add_piece(column)
            for _ in range(game_two.width - 1):
                game_two.undo()
            after_undo_board = game_two.board
        except ValueError:
            self.fail("undo function raised an error on good input.")
        self.assertEqual(before_add_board, after_undo_board)

    def test_is_game_over_vertically(self):
        '''
        test_is_game_over_vertically
        A function that is designed to test whether the hand made vertical
            four piece in line board with "X" or "O" as the winner can match
            the winner and end of game in the is_game_over function in
            connect_four.py
        Returns: Nothing
        '''
        # Test 1 with "X" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                      [' ', ' ', ' ', 'X', 'O', ' ', ' ']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("X", game.win)
        # Test 2 with "O" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
                      ['X', ' ', ' ', ' ', ' ', ' ', 'O'],
                      ['X', ' ', ' ', ' ', ' ', ' ', 'O'],
                      ['X', ' ', ' ', ' ', ' ', 'X', 'O']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("O", game.win)

    def test_is_game_over_horizontally(self):
        '''
        test_is_game_over_horizontally
        A function that is designed to test whether the hand made horizontal
            four piece in line board with "X" or "O" as the winner can match
            the winner and end of game in the is_game_over function in
            connect_four.py
        Returns: Nothing
        '''
        # Test 1 with "X" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
                      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
                      ['X', 'X', 'X', 'X', ' ', ' ', 'O']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("X", game.win)
        # Test 2 with "O" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'X', 'X', 'O', ' ', ' '],
                      [' ', 'O', 'X', 'O', 'X', ' ', ' '],
                      [' ', 'O', 'O', 'O', 'X', ' ', ' '],
                      [' ', 'O', 'X', 'X', 'O', 'X', ' ']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("O", game.win)

    def test_is_game_over_diagonally(self):
        '''
        test_is_game_over_diagonally
        A function that is designed to test whether the hand made diagonal
            four piece in line board with "X" or "O" as the winner can match
            the winner and end of game in the is_game_over function in
            connect_four.py
        Returns: Nothing
        '''
        # Check left to right diagonals with "X" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', 'X', ' ', ' '],
                      [' ', 'O', 'X', 'X', 'O', ' ', ' '],
                      [' ', 'O', 'X', 'O', 'O', ' ', ' '],
                      [' ', 'X', 'O', 'O', 'X', ' ', ' ']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("X", game.win)
        # Check right to left diagonals with "O" as the winner
        game = c.ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'X', 'X', 'O', ' ', ' '],
                      [' ', 'O', 'X', 'O', 'X', ' ', ' '],
                      [' ', 'O', 'O', 'O', 'X', ' ', ' '],
                      [' ', 'O', 'X', 'X', 'O', 'X', ' ']]
        bool_result = game.is_game_over()
        self.assertTrue(bool_result)
        self.assertEqual("O", game.win)

    def test_get_winner(self):
        '''
        test_get_winner
        A function that is designed to test whether the hand made examples with
            winners can match the winners in the is_game_over function in
            connect_four.py
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # Test 1 with "X" as the winner
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', 'X', ' ', ' '],
                      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                      [' ', ' ', 'X', 'X', 'O', ' ', ' '],
                      [' ', 'X', 'O', 'O', 'O', 'X', ' ']]
        actual_winner = game.get_winner()
        self.assertEqual("X", actual_winner)
        # Test 2 with "O" as the winner
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                      [' ', ' ', 'X', 'X', ' ', ' ', ' '],
                      [' ', 'X', 'O', 'O', 'O', 'O', ' ']]
        actual_winner = game.get_winner()
        self.assertEqual("O", actual_winner)
        # Test 3 with no one (None) as the winner
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                      [' ', 'O', 'O', 'O', ' ', ' ', ' '],
                      [' ', 'X', 'X', 'O', ' ', ' ', ' '],
                      [' ', 'X', 'X', 'O', ' ', ' ', ' ']]
        actual_winner = game.get_winner()
        self.assertEqual(None, actual_winner)

    def test_str_(self):
        '''
        test_get_winner
        A function that is designed to test whether hand made board can
            be printed as the print_out_graph string using the __str__
            function in connect_four.py
        Returns: Nothing
        '''
        game = c.ConnectFour()
        # Test 1
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'O', ' ', ' ', ' ', ' '],
                      ['X', 'X', 'X', 'X', 'O', ' ', ' '],
                      ['X', 'O', 'O', 'O', 'X', ' ', ' ']]
        actual_graph = game.__str__()
        print_out_graph = "| | | | | | | |\n---------------\n" \
                          "| | | | | | | |\n---------------\n" \
                          "| | | | | | | |\n---------------\n" \
                          "| | |O| | | | |\n---------------\n" \
                          "|X|X|X|X|O| | |\n---------------\n" \
                          "|X|O|O|O|X| | |\n---------------\n"
        self.assertEqual(actual_graph, print_out_graph)
        # Test 2
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                      [' ', ' ', 'X', 'X', ' ', ' ', ' '],
                      [' ', ' ', 'O', 'X', ' ', ' ', ' '],
                      [' ', 'X', 'O', 'X', 'O', ' ', ' ']]
        actual_graph = game.__str__()
        print_out_graph = "| | | | | | | |\n---------------\n" \
                          "| | | | | | | |\n---------------\n" \
                          "| | | |O| | | |\n---------------\n" \
                          "| | |X|X| | | |\n---------------\n" \
                          "| | |O|X| | | |\n---------------\n" \
                          "| |X|O|X|O| | |\n---------------\n"
        self.assertEqual(actual_graph, print_out_graph)


def main():
    unittest.main(verbosity=3)


if __name__ == '__main__':
    main()
