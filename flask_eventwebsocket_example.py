from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import click

app = Flask(__name__)

PORT = 8000

@app.route('/')
def index():
    return render_template('index.html', port=PORT)

@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.receive()
            ws.send(message)
    return

@click.command()
@click.option('--port', '-P', default='8000')
def server_loop(port):
    http_server = WSGIServer(('', int(port)), app, handler_class=WebSocketHandler)
    http_server.serve_forever()

if __name__ == '__main__':
    server_loop()
