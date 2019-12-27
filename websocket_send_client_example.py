import threading
import websocket
import time

HOST='localhost'
PORT=8000


def on_message(ws, message):
    print("on_message:{}".format(message))


def on_open(ws):
    def run(*args):
        i = 1
        while True:
            message = "Message {}".format(i)
            print("send:{}".format(message))
            ws.send(message)
            time.sleep(1)
            i += 1
        ws.close()  # not reach
    threading.Thread(target=run).start()


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://{}:{}/api".format(HOST, PORT))
    ws.on_message = on_message
    ws.on_open = on_open
    ws.run_forever()
