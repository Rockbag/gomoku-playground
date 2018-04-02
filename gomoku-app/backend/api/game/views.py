import json

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.http import require_POST

from api.game.const import BOARD_DEPTH_WIDTH_MAX
from api.game.game_service import create_new_game
from api.game.validators import game_board_size_validator
from api.models import Game


@require_POST
def create_game(request):
    """Creates a new game room with an empty state."""
    request_data = json.loads(request.body.decode('utf-8'))
    board_cols = request_data.get('board_cols', 0)
    board_rows = request_data.get('board_rows', 0)
    player = request.user

    if not player.is_authenticated:
        return _unauthorized_response()

    try:
        game_board_size_validator(board_cols)
        game_board_size_validator(board_rows)
    except ValidationError:
        return _game_creation_invalid_board_input_response()

    game_rooms_with_player = Game.objects.filter(Q(player_one=player) | Q(player_two=player))
    if game_rooms_with_player:
        return _user_is_already_in_a_room_response(game_rooms_with_player)

    game_state = create_new_game(player, board_cols, board_rows)
    return HttpResponse(content=json.dumps({'game_id': str(game_state.id)}), content_type='application/json')


def _unauthorized_response():
    response_data = _generate_error_message('User is not logged in',
                                            'UNAUTHORIZED')

    return HttpResponseForbidden(response_data, content_type='application/json')


def _user_is_already_in_a_room_response(game_rooms):
    response_data = _generate_error_message('User is already in room: {}'.format(game_rooms[0].id),
                                            'USER_ALREADY_IN_ROOM')
    return HttpResponseBadRequest(response_data, content_type='application/json')


def _game_creation_invalid_board_input_response():
    response_data = _generate_error_message('Board column and row size must be between 0 and {max_board_depth_width}'
                                            .format(max_board_depth_width=BOARD_DEPTH_WIDTH_MAX),
                                            error_code='INVALID_BOARD_SIZE')
    return HttpResponseBadRequest(response_data, content_type='application/json')


def _generate_error_message(error_message, error_code):
    return json.dumps({'status': 'error',
                       'error_code': error_code,
                       'error_message': error_message})
