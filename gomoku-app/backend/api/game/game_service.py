from api.models import Game


def create_new_game(creator, cols, rows):
    return Game.objects.create(player_one=creator,
                               board_cols=cols,
                               board_rows=rows,
                               board_state=_generate_empty_board(cols, rows))


def _generate_empty_board(cols, rows):
    return '0' * (cols * rows)
