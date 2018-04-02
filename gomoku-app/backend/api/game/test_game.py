import json
import re

from django.contrib.auth.models import User
from django.test import Client, TestCase

from api.game.const import BOARD_DEPTH_WIDTH_MAX
from api.models import Game


class GameStateCreationTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_game_is_created(self):
        # Given there's an existing player
        player_one = User.objects.create_user('test1', 'test1@test.com', '1234')
        # And the player is logged in
        self.client.login(username='test1', password='1234')
        # When they create a new game
        response = self.client.post('/game/',
                                    data=json.dumps({'board_cols': 10,
                                                     'board_rows': 10}),
                                    content_type='application/json')

        # Then the game state should be created
        self.assertContains(response, 'game_id', 1)
        # And the game state should be empty
        game_id = json.loads(response.content)['game_id']
        game = Game.objects.get(id=game_id)
        board_state = game.board_state
        empty_state = re.match('0{%s}' % (game.board_rows * game.board_cols),
                               board_state)
        self.assertTrue(empty_state)
        # And the game board should have the correct amount of fields
        self.assertEqual(len(board_state), game.board_rows * game.board_cols)
        # And the game state should only have one player in it
        self.assertIsNone(game.player_two)

    def test_invalid_input_rows(self):
        User.objects.create_user('test1', 'test1@test.com', '1234')
        self.client.login(username='test1', password='1234')
        response = self.client.post('/game/',
                                    data=json.dumps({'board_cols': 10,
                                                     'board_rows': 0}),
                                    content_type='application/json')
        self.assertIn('Board column and row size must be between 0 and {}'.format(BOARD_DEPTH_WIDTH_MAX),
                      response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 400)

    def test_invalid_input_cols(self):
        User.objects.create_user('test1', 'test1@test.com', '1234')
        self.client.login(username='test1', password='1234')
        response = self.client.post('/game/',
                                    data=json.dumps({'board_cols': 25,
                                                     'board_rows': 10}),
                                    content_type='application/json')
        self.assertIn('Board column and row size must be between 0 and {}'.format(BOARD_DEPTH_WIDTH_MAX),
                      response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 400)

    def test_unauthenticated_player(self):
        response = self.client.post('/game/',
                                    data=json.dumps({'board_cols': 10,
                                                     'board_rows': 10}),
                                    content_type='application/json')

        self.assertIn('User is not logged in', response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 403)

    def test_only_one_room_at_a_time(self):
        # Given a user who is already in a room
        user = User.objects.create_user('in-a-room-already', 'test@test.com', '1234')
        game = Game.objects.create(player_one=user,
                                   board_cols=10,
                                   board_rows=10)

        self.client.login(username='in-a-room-already', password='1234')
        response = self.client.post('/game/', data=json.dumps({'board_cols': 10,
                                                               'board_rows': 10}),
                                    content_type='application/json')
        self.assertIn('User is already in room: {room_id}'.format(room_id=game.id), response.content.decode('utf-8'))

