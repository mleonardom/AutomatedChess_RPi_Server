import json
import falcon

from server.chess.Game import Game
from server.chess.AbstractResource import AbstractResource

class GameResource(AbstractResource):

    default_elo = 1500
    default_depth = 10
    default_threads = 2

    game = Game()

    def on_get(self, req, resp):
        if not self.game.is_in_game(): 
            self._response_no_game_error(resp)
            return

        doc = {
            'visual': self.game.get_board_visual()
        }

        self._response200(resp, doc)
    
    def on_post(self, req, resp):
        if not self.game.is_in_game(): 
            self._response_no_game_error(resp)
            return

        raw_data = json.load(req.bounded_stream)
        move = raw_data.get("move")

        if move:
            stockfish_move = None
            try:
                stockfish_move = self.game.move(move)
            except:
                pass
            doc = {
                "stockfish_move": stockfish_move
            }
            self._response200(resp, doc)
        else:
            self._response400(resp, "Debe especificar un movimiento");
    
    def on_put(self, req, resp):
        raw_data = json.load(req.bounded_stream)
        elo = raw_data.get("elo", self.default_elo)
        depth = raw_data.get("depth", self.default_depth)
        threads = raw_data.get("threads", self.default_threads)

        if elo < 1320 or elo > 3190:
            self._response400(resp, "elo must be between 1320 and 3190")
            return
        if depth < 0 or depth > 80:
            self._response400(resp, "depth must be between 0 and 80")
            return
        if threads < 0 or threads > 6:
            self._response400(resp, "threads must be between 0 and 4")
            return

        self.game.new_game(elo, depth, threads)

        self._response200(resp, self.game.get_parameters())