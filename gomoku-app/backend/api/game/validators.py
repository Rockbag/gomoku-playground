from django.core.exceptions import ValidationError

from api.game.const import BOARD_DEPTH_WIDTH_MAX


def game_board_size_validator(value):
    if not 0 < value <= BOARD_DEPTH_WIDTH_MAX:
        raise ValidationError('Row and Column size must be between 0 and {max_value}'.format(max_value=BOARD_DEPTH_WIDTH_MAX))
