import json
import falcon


class AbstractResource:

    def _response200(self, resp, doc):
        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
    
    def _response400(self, resp, error):
        doc = {
            "error": error
        }
        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_400

    def _response_no_game_error(self, resp):
        self._response400(resp, "No hay un juego en curso")
        