# lab-04 > websocket > ⚙️ client.py > ⦿ WebSocketClient > ⚙️ on_message

import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Connecting...")
        tornado.websocket.websocket_connect(
            url=f"ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

    # FIX: Thụt đầu dòng hai phương thức này vào bên trong lớp WebSocketClient
    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()
            # Bắt đầu đọc tin nhắn ngay sau khi kết nối thành công
            self.connection.read_message(callback=self.on_message)
        except Exception as e:
            print(f"Could not connect ({e}), retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return

        print(f"Received word from server: {message}")

        # Tiếp tục lắng nghe tin nhắn tiếp theo
        if self.connection:
            self.connection.read_message(callback=self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()

    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)

    io_loop.start()

if __name__ == "__main__":
    main()