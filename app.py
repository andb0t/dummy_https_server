import os

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "This is the home page"


if __name__ == '__main__':
    _port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=_port)
