"""Websocket client"""
import _thread
import time
import websocket
# https://github.com/websocket-client/websocket-client


HOST = 'ws://echo.websocket.org'


def on_message(ws_, message):
    print('Message: {}'.format(message))


def on_error(ws_, error):
    print('We got an error: {}'.format(error))


def on_close(ws_):
    print('Websockets closed.')


def on_open(ws_):
    def run(*args):
        for i in range(3):
            ws.send('Hello {}'.format(i))
            time.sleep(1)

        time.sleep(1)
        ws_.close()
        print('Thread terminating ...')

    print('Starting new thread')
    _thread.start_new_thread(run, ())


if __name__ == '__main__':
    # ws = websocket.WebSocket(sslopt={'check_hostname': False})
    # ws.connect('wss://echo.websocket.org')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        HOST, on_message=on_message, on_error=on_error, on_close=on_close,
        on_open=on_open
    )
    ws.run_forever(sslopt={'check_hostname': False})
