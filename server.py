import asyncio
import logging

import websockets

CONNECTIONS = []

async def welcome(websocket, path):
    CONNECTIONS.append(websocket)
    await websocket.recv()
    print(f"Client connected! {websocket}")


class Server():
    def __init__(self, host="localhost", port=8765):
        self.start_server = websockets.serve(welcome, host, port)
        self.loop = asyncio.get_event_loop()

    def start(self):
        self.loop.run_until_complete(self.start_server)
        self.loop.run_forever()

    def stop(self):
        self.loop.stop()

    async def send(self, message):
        await CONNECTIONS[0].send(message)

class sender():
    def __init__(self):
        self.server = Server()
        asyncio.ensure_future(self._send(), loop=self.server.loop)
        self.server.start()

    async def _send(self):
        while not CONNECTIONS:
            await asyncio.sleep(1)
        
        for i in range(10):
            print(f"send {i}")
            try:
                await self.server.send(f"{i}")
            except Exception as e:
                print(type(e), e)
            
            await asyncio.sleep(1)

        self.server.stop()


if __name__ == "__main__":
    send = sender()
