"""A dummy app."""
import os
import sys

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    """Return simple string."""
    return "This is the home page"


@app.route('/api/dummy/', methods=['GET'])
def return_dummy_json():
    """Request dummy results."""
    dummy_dict = {'info': 'Hello Hyve', 'more_info': 'It seems to work', 'even_more_info': 'no HTTPS...yet!'}
    return flask.jsonify(dummy_dict)


if __name__ == '__main__':
    if not sys.argv:
        _port = int(os.environ.get('PORT', 8080))
    else:
        _port = sys.argv[1]
    app.run(host='0.0.0.0', port=_port)
