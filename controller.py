import logging

from flask import Response, jsonify

from tictactoe import Board, configure_logger, INVALID_MOVE_ERROR_MSG
from tictactoe.model import Model
from tictactoe.view import View


MODEL = Model()
VIEW = View()


logger = logging.getLogger(__name__)
configure_logger()


def get_board_state() -> Response:
    """
    Retrieves the current state of the board.

    Returns
    -------
    Response
        A Flask response object containing the board state as JSON.
    """
    logger.debug('Fetching the current board state.')
        
    # Get the board state from the model
    board_state = MODEL.get_board_state()
        
    # Return the board state as a JSON response
    logger.debug(f'Returning board state: {board_state}')
    return jsonify({'board': board_state})

def get_winner() -> Response:
    """
    Retrieves the winner of the game, if there is one.

    Returns
    -------
    Response
        A Flask response object containing the winner as JSON.
    """
    logger.debug('Fetching the winner of the game.')
        
    # Get the winner from the model
    winner = MODEL.get_winner()
        
    # Return the winner as a JSON response
    logger.debug(f'Returning winner: {winner}')
    return jsonify({'winner': winner})

def validate_index(index: str) -> int:
    """
    Validates the provided index for a move.

    Parameters
    ----------
    index : str
        The index to validate.

    Returns
    -------
    int
        The validated index.

    Raises
    ------
    ValueError
        If the index is not a valid integer or is out of bounds.
    """
    logger.debug(f'Validating move index: {index}')
        
    try:
        # Convert the index to an integer
        idx = int(index)
            
        # Check if the index is within the valid range
        if idx < 0 or idx >= 9:
            logger.error(f'Invalid move index: {index}')
            raise ValueError(INVALID_MOVE_ERROR_MSG)
            
        logger.debug(f'Validated index: {idx}')
        return idx
    except ValueError:
        logger.error(f'Error converting index to integer or out of bounds: {index}')
        raise ValueError(INVALID_MOVE_ERROR_MSG)

def make_move(index: str) -> Response:
    """
    Makes a move at the specified index.

    Parameters
    ----------
    index : str
        The index at which to make the move.

    Returns
    -------
    Response
        A Flask response object indicating success or failure.
    """
    logger.debug(f'Attempting to make a move at index: {index}')
        
    try:
        # Validate the index and make the move
        idx = validate_index(index)
        MODEL.make_move(idx)
            
        # Return a success response with the updated board state
        logger.info(f'Move successful at index: {idx}')
        return jsonify({'success': True, 'board': MODEL.get_board_state()})
    except ValueError as e:
        # Log the error and return an error response
        logger.error(f'Error making move: {e}')
        return VIEW.error(str(e), 400)
