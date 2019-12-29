import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

class Server():
    def __init__(self, host="localhost", port=8765):
        self.start_server = websockets.serve(hello, host, port)
        self.loop = asyncio.get_event_loop()

    def start(self):
        self.loop.run_until_complete(self.start_server)
        self.loop.run_forever()

if __name__ == "__main__":
    server = Server()
    server.start()
