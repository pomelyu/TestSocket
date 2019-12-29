import logging
import asyncio
import websockets

class Client():
    def __init__(self, uri="ws://localhost:8765"):
        self.uri = uri
        self.con = None
        self.loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.connect_object(), loop=self.loop)
        asyncio.ensure_future(self.handle_message(), loop=self.loop)
        self.loop.run_forever()
        # self.loop.run_until_complete(self.connect_object())

    async def connect_object(self):
        # async with websockets.connect(self.uri) as socket:
        #     while True:
        #         try:
        #             message = await socket.recv()
        #             print(f"received {message}")
        #         except Exception as e:
        #             print(type(e), e)
                    
        #         await asyncio.sleep(1)

        self.con = await websockets.connect(self.uri)

    async def handle_message(self):
        while not self.con:
            await asyncio.sleep(1)
            print("zz")

        while True:
            try:
                message = await self.con.recv()
                print(f"received {message}")
            except Exception as e:
                print(e)
                
            await asyncio.sleep(1)

if __name__ == "__main__":
    client = Client()


# async def hello():
#     uri = "ws://localhost:8756"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             try:
#                 print("XX")
#                 message = await websocket.recv()
#                 print(message)
#             except:
#                 pass

#         # name = input("What's your name? ")

#         # await websocket.send(name)
#         # print(f"> {name}")

#         # greeting = await websocket.recv()
#         # print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())
