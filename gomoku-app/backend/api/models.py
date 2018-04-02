import uuid

from django.contrib.auth.models import User
from django.db import models

from api.game.const import BOARD_DEPTH_WIDTH_MAX


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_one = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='player_one', db_index=True)
    player_two = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='player_two', null=True, blank=True, db_index=True)
    board_cols = models.IntegerField()
    board_rows = models.IntegerField()
    board_state = models.CharField(max_length=BOARD_DEPTH_WIDTH_MAX * BOARD_DEPTH_WIDTH_MAX)
