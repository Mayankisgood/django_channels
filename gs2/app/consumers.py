from channels.consumer import SyncConsumer,AsyncConsumer

from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect',event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
            print("web_socket ..receive",event)
            print("message is..........",event["text"])
            # client server ko bhejat hai ye ---
        #     self.send({
        #     'type':'websocket.send',
        #     'text':'message sent to client'
        # })
    def websocket_disconnect(self,event):
            print("websocket_disconnect",event)
            #  took too long to shut down and was killed. ye na aaye iske liye
            raise StopConsumer()
            
            
            
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect',event)
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self,event):
        print("web_socket ..receive",event)
    async def websocket_disconnect(self,event):
        print("websocket_disconnect",event)
        raise StopConsumer()
    