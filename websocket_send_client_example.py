import websocket

HOST='localhost'
PORT=8000

import _thread as thread
import time

def on_message(ws, message):
    print("on_message:{}".format(message))

def on_open(ws):
    def run(*args):
        for i in range(3):
            message = "Hello {}".format(i)
            print("send:{}".format(message))
            ws.send(message)
            time.sleep(1)
        ws.close()
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://{}:{}/api".format(HOST, PORT))
    ws.on_message = on_message
    ws.on_open = on_open
    ws.run_forever()
