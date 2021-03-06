# Generated by Django 2.0.2 on 2018-04-02 16:25

import api.game.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('board_cols', models.IntegerField(validators=[api.game.validators.game_board_size_validator])),
                ('board_rows', models.IntegerField(validators=[api.game.validators.game_board_size_validator])),
                ('board_state', models.CharField(max_length=400)),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_one', to=settings.AUTH_USER_MODEL)),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
