import falcon
from server.chess.ChessResources import GameResource

app = application = falcon.App()

chessGame = GameResource()

app.add_route('/chess/game', chessGame)


if __name__ == '__main__':
    with make_server('', 8081, app) as httpd:
        print('Serving on port 8081...')

        httpd.serve_forever()