import logging

from flask import jsonify, make_response, Response
from tictactoe import Board

logger = logging.getLogger(__name__)

class View:
    """
    A class to represent the view for the Tic Tac Toe game.

    Methods
    -------
    board_state(board: Board) -> Response:
        Returns the current state of the board as a JSON response.

    get_winner(winner: str = None) -> Response:
        Returns the winner of the game as a JSON response.

    error(error: str) -> Response:
        Returns an error message as a JSON response.
    """

    def board_state(self, board: Board) -> Response:
        """
        Returns the current state of the board as a JSON response.

        Parameters
        ----------
        board : Board
            The current state of the Tic Tac Toe board.

        Returns
        -------
        Response
            A Flask response object containing the board state.
        """
        #board_state = board
        logging.debug("Returning the current board state as a JSON response.")
        
        # Convert the board state to JSON format and return it
        return jsonify({'board': board.squares})

    def get_winner(self, winner: str = None) -> Response:
        """
        Returns the winner of the game as a JSON response.

        Parameters
        ----------
        winner : str, optional
            The winner of the game (default is None).

        Returns
        -------
        Response
            A Flask response object containing the winner.
        """
        logging.debug(f'Returning the winner as a JSON response: {winner}')
        
        # Return the winner in JSON format
        return jsonify({'winner': winner})

    def error(self, error: str) -> Response:
        """
        Returns an error message as a JSON response.

        Parameters
        ----------
        error : str
            The error message to return.

        Returns
        -------
        Response
            A Flask response object containing the error message.
        """
        logging.error(f'Returning an error message as a JSON response: {error}')
        
        # Return the error message in JSON format with a 400 status code
        return make_response(jsonify({'error': error}), 400)
