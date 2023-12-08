from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
import asyncio

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("web socket connected..")
        # when data receive from client
        self.accept()
        # self.close()  --- ye kahi bhi forcefully rejection ke liye karte hai
        # self.close(code =4233)  --- ye error code show karna ho to
    def receive(self, text_data=None,bytes_data=None):
        print('message received from client',text_data)
        # server client ko bhejega
        for i in range(4):
            self.send(text_data=str(i))
            sleep(1)
        # self.send(bytes_data=data)  to send client binary frame
    def disconnect(self, close_code):
        print('websocket disconnected',close_code)
        


class MyAsyncWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("web socket connected..")
        # when data receive from client
        await self.accept()
        # self.close()  --- ye kahi bhi forcefully rejection ke liye karte hai
        # self.close(code =4233)  --- ye error code show karna ho to
    async def receive(self, text_data=None,bytes_data=None):
        print('message received from client',text_data)
        # server client ko bhejega
        for i in range(10):
            await self.send(text_data=str(i))
            await asyncio.sleep(1)
    # self.send(bytes_data=data)  to send client binary frame
    async def disconnect(self, close_code):
        await print('websocket disconnected',close_code)