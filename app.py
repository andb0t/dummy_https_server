"""A dummy app."""
import os
import json

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    """Return simple string."""
    return "This is the home page"


@app.route('/api/dummy/', methods=['GET'])
def return_dummy_json():
    """Request dummy results."""
    dummy_dict = {'info': 'hello', 'more_info': 'It seems to work'}
    return flask.jsonify(dummy_dict)


if __name__ == '__main__':
    _port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=_port)
