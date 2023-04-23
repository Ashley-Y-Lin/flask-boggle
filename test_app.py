from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config["TESTING"] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get("/")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board">', html)
            ...
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            response = client.post("/api/new-game")
            json = response.get_json()
            game_id = json["gameId"]
            board = json["board"]

            self.assertIsInstance(game_id, str)
            self.assertIsInstance(board, list)
            self.assertIsInstance(board[0], list)

            self.assertIn(game_id, games)

            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # test that the game_id is a string
            # test that the board is a list
            # test that the game_id is in the dictionary of games (imported from app.py above)

    def test_score_word(self):
        """Test if word is valid"""

        with self.client as client:
            ...
            response = client.post("/api/new-game")
            json = response.get_json()
            game_id = json["gameId"]

            game = games[game_id]
            game.board = [
                ["I", "S", "E", "M", "E"],
                ["N", "S", "D", "S", "G"],
                ["B", "O", "A", "R", "P"],
                ["G", "S", "P", "A", "X"],
                ["Y", "X", "B", "E", "C"],
            ]

            t1 = client.post(
                "/api/score-word", json={"gameId": game_id, "word": "BOARD"}
            )
            t1json = t1.get_json()
            self.assertEqual(t1json, {"result": "ok"})

            t2 = client.post(
                "/api/score-word", json={"gameId": game_id, "word": "WEIRD"}
            )
            t2json = t2.get_json()
            self.assertEqual(t2json, {"result": "not-on-board"})

            t3 = client.post(
                "/api/score-word", json={"gameId": game_id, "word": "GHINWEKA"}
            )
            t3json = t3.get_json()
            self.assertEqual(t3json, {"result": "not-word"})

            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # find that game in the dictionary of games (imported from app.py above)

            # manually change the game board's rows so they are not random

            # test to see that a valid word on the altered board returns {'result': 'ok'}
            # test to see that a valid word not on the altered board returns {'result': 'not-on-board'}
            # test to see that an invalid word returns {'result': 'not-word'}
