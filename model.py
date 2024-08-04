import logging
from typing import Optional

from tictactoe import Board, SQUARE_OCCUPIED_ERROR_MSG

logger = logging.getLogger(__name__)

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
        self.board = Board()
        self.player = 'X'
        self.winner = None

    def get_current_player(self) -> str:
        """
        Returns the current player.

        Returns
        -------
        str
            The current player ('X' or 'O').
        """
        return self.board.getPlayer

    def change_player(self) -> None:
        """
        Switches the current player from 'X' to 'O' or from 'O' to 'X'.
        """
        if self.player == 'X':
            self.player = 'O'
        elif self.player == 'O':
            self.player = 'X'
            
        self.board.setPlayer
        

    def set_winner(self) -> None:
        """
        Checks for a winner and sets the winner attribute if there is one.
        """
        self.winner = self.board.winner

    def get_winner(self) -> Optional[str]:
        """
        Returns the winner of the game (if any).

        Returns
        -------
        Optional[str]
            The winner of the game, or None if there is no winner yet.
        """
        return self.winner

    def get_board_state(self) -> list[str]:
        """
        Returns a copy of the current board state.

        Returns
        -------
        list[str]
            A copy of the current board state.
        """
        return self.board.get_state()

    def move(self, index: int) -> None:
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
        if True:
            if self.board.is_square_empty(index):
                self.board.set_square(index, self.player)
                self.set_winner()
                if not self.winner:
                    self.change_player()
        else:   
            logger.error(f'Move failed at index {index} - square already occupied')
            raise ValueError(SQUARE_OCCUPIED_ERROR_MSG)
