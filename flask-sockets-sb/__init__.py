import random

from flask import Flask, render_template, request
from flask_sockets import Sockets


RESPONSES = [
    'Got it', 'Yup I heard you', 'Yes', 'Affirmative', 'Acknowledged',
    'Alright', 'Good stuff', 'Roger that', 'Cool story', 'Ok'
]

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('Submitted a POST request')

    return render_template('index.html')


@sockets.route('/echo')
def socket_echo(ws):
    print('Inside socket echo')
    while not ws.closed:
        message = ws.receive()
        print('Received message from client: "{}"'.format(message))

        response = '{} wrt "{}"'.format(random.choice(RESPONSES), message)
        ws.send(response)
        print('Sent "{}" from server to client'.format(response))


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
    # in prod, replace this with gunicorn
