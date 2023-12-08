from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer

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
        self.send(text_data="message from server to client")
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
        await self.send(text_data="message from server to client")
    # self.send(bytes_data=data)  to send client binary frame
    async def disconnect(self, close_code):
        await print('websocket disconnected',close_code)