from stockfish import Stockfish

stockfish_default_parameters = {
    "Hash": 2048
}

global stockfishGame
global userColor

class Game:

    def is_in_game(self):
        global stockfishGame
        try:
            stockfishGame
        except:
            return False
        return True

    def new_game(self, user_color, elo, depth, threads):
        global stockfishGame
        global userColor

        userColor = user_color
        # elo between 1320 and 3190
        stockfishGame = Stockfish(path="/usr/games/stockfish", depth=depth, parameters=stockfish_default_parameters)
        stockfishGame.update_engine_parameters({"Threads": threads})
        stockfishGame.set_elo_rating(elo)

        stockfish_move = self.stockfish_move() if userColor == "BLACK" else None

        return {
            "engine_parameters": self.get_parameters(),
            "stockfish_move": stockfish_move
        }
    
    def get_board_visual(self):
        global stockfishGame

        return stockfishGame.get_board_visual()
    
    def get_fen_position(self):
        global stockfishGame

        return stockfishGame.get_fen_position()
    
    def get_evaluation(self):
        global stockfishGame

        return stockfishGame.get_evaluation()
    
    def get_parameters(self):
        global stockfishGame

        return stockfishGame.get_engine_parameters()
    
    def move(self, move):
        global stockfishGame
        stockfishGame.make_moves_from_current_position([move])

        return self.stockfish_move()

    def stockfish_move(self):
        global stockfishGame
        stockfish_move = stockfishGame.get_best_move()
        stockfishGame.make_moves_from_current_position([stockfish_move])

        return stockfish_move
    
    def is_move_correct(self, move):
        return stockfishGame.is_move_correct(move)
