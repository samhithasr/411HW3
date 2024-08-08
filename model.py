import logging
from typing import Optional

from tictactoe import Board, SQUARE_OCCUPIED_ERROR_MSG

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)

class Model:
    """
    A class to represent the model for the Tic Tac Toe game.

    Attributes
    ----------
    board : Board
        The current state of the Tic Tac Toe board.
    player : str
        The current player ('X' or 'O').
    winner : Optional[str]
        The winner of the game (if any).

    Methods
    -------
    get_current_player() -> str:
        Returns the current player.

    change_player() -> None:
        Switches the current player.

    set_winner() -> None:
        Checks for a winner and sets the winner attribute if there is one.

    get_winner() -> Optional[str]:
        Returns the winner of the game (if any).

    get_board_state() -> list[str]:
        Returns a copy of the current board state.

    move(index: int) -> None:
        Makes a move at the specified index, changes the player, and checks for a winner.
    """
    
    def __init__(self):
        """
        Initializes the Model with an empty board and sets the starting player to 'X'.
        """
        logging.debug('Initializing the Model with an empty board and setting the starting player to "X".')

        # Create an empty board with 9 squares
        squares = []
        for i in range(9):
            squares.append('')
        logging.debug(f'Board initialized with squares: {squares}')

        # Set up the board
        self.board = Board(squares)
        logging.debug('Board object created and assigned to self.board.')

        # Set the starting player to 'X'
        self.player = 'X'
        logging.debug(f'Starting player set to: {self.player}')

        # Initialize the winner to None
        self.winner = None
        logging.debug('Winner initialized to None.')

    def get_current_player(self) -> str:
        """
        Returns the current player.

        Returns
        -------
        str
            The current player ('X' or 'O').
        """
        logging.debug(f'Fetching the current player: {self.player}')
        
        # Return the current player ('X' or 'O')
        return self.player

    def change_player(self) -> None:
        """
        Switches the current player from 'X' to 'O' or from 'O' to 'X'.
        """
        logging.debug(f'Current player before change: {self.player}')
        print("hello this is mike")

        # Switch the player from 'X' to 'O' or from 'O' to 'X'
        if self.player == 'X':
            self.player = 'O'
            logging.debug('Player changed from "X" to "O".')
        else:
            self.player = 'X'
            logging.debug('Player changed from "O" to "X".')

    def set_winner(self) -> None:
        """
        Checks for a winner and sets the winner attribute if there is one.
        """
        # Initialize winner to None
        self.winner = None
        logging.debug('Winner initialized to None. Beginning check for a winner.')

        # Check rows for a winner
        for i in range(0, 6, 3):
            if self.board.squares[i] == self.board.squares[i + 1] == self.board.squares[i + 2] != '':
                self.winner = self.board.squares[i]
                logging.debug(f'Winner found in row starting at index {i}: {self.winner}')
                return

        # Check columns for a winner    
        for i in range(3):
            if self.board.squares[i] == self.board.squares[i + 3] == self.board.squares[i + 6] != '':
                self.winner = self.board.squares[i]
                logging.debug(f'Winner found in column starting at index {i}: {self.winner}')
                return

        # Check diagonals for a winner
        if self.board.squares[0] == self.board.squares[4] == self.board.squares[8] != '':
            self.winner = self.board.squares[4]
            logging.debug(f'Winner found in diagonal from index 0 to 8: {self.winner}')
            return
        elif self.board.squares[2] == self.board.squares[4] == self.board.squares[6] != '':
            self.winner = self.board.squares[4]
            logging.debug(f'Winner found in diagonal from index 2 to 6: {self.winner}')
            return
        
        logging.debug('No winner found after checking all rows, columns, and diagonals.')

    def get_winner(self) -> Optional[str]:
        """
        Returns the winner of the game (if any).

        Returns
        -------
        Optional[str]
            The winner of the game, or None if there is no winner yet.
        """
        logging.debug(f"Fetching the current winner: {self.winner}")
        
        # Return the winner of the game, or None if there is no winner yet
        return self.winner

    def get_board_state(self) -> list[str]:
        """
        Returns a copy of the current board state.

        Returns
        -------
        list[str]
            A copy of the current board state.
        """
        logging.debug(f'Fetching the current board state: {self.board}')

        # Return a copy of the current board state to avoid external modifications
        return self.board.squares

    def move(self,index: int) -> None:
        """
        Makes a move at the specified index, changes the player, and checks for a winner.

        Parameters
        ----------
        index : int
            The index at which to make the move.

        Raises
        ------
        ValueError
            If the specified index is already occupied.
        """
        logging.debug(f'Attempting to make a move at index {index} by player {self.player}.')
        
        if self.board.squares[index] == "":
            # Make the move by setting the square to the current player's symbol
            self.board.squares[index] = self.player
            logging.info(f'Player {self.player} made a move at index {index}.')

            # Check if the move resulted in a winner
            self.set_winner()
            logging.debug('Checked for a winner after the move.')

            # Switch to the other player
            self.change_player()
            logging.debug(f'Player changed after move. Next player: {self.player}')
        else:   
            # Log an error if the square is already occupied and raise a ValueError
            logging.error(f'Move failed at index {index} - square already occupied.')
            raise ValueError(SQUARE_OCCUPIED_ERROR_MSG)
