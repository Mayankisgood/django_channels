from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync
import channels
import uuid
import json 

class MyWebsocketConsumer(WebsocketConsumer):
    # def __init__(self,channel_name):
    def connect(self):
        print("web socket connected..")
        print("channel_layer",self.channel_layer)
       
        self.group_name = self.scope['url_route']['kwargs']['groupkaName']
        self.channel_name = f"websocket_{self.group_name}_{str(uuid.uuid4())}"
        print("channel_name", self.channel_name)
        print("Group_name",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        
    def receive(self, text_data=None,bytes_data=None):
        print('message received from client',text_data)
        data = json.loads(text_data)
        print(data,"data")
        # message = 
        
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type" : "chat.message",    
                "message" : data["msg"]
            }
        )

            
        
    # def chat_message(self, event):
    #     print("event",event)
    #     self.send(text_data=json.dumps({
    #         'msg':event['message']
    #     }    
    #     ))
    
    def chat_message(self, event):
        print("event",event)
        self.send(text_data=json.dumps(
             {
                'type':'websocket.send',
                'text':event['message']
            }
    
        ))
    
    # def chat_message(self,event):
    #     print('event......',event)
    #     print('actual_data..',event['message'])
    #     print('type of actual_data..',type(event['message']))
    #     self.send(
    #         {
    #             'type':'websocket.send',
    #             'text':event['message']
    #         }
    #     )


        

    def disconnect(self, close_code):
        print('websocket disconnected',close_code)
        


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("web socket connected..")
        # when data receive from client
        await self.accept()

    async def receive(self, text_data=None,bytes_data=None):
        print('message received from client',text_data)
        # server client ko bhejega
        for i in range(10):
            await self.send(text_data=str(i))
            await asyncio.sleep(1)
    # self.send(bytes_data=data)  to send client binary frame
    async def disconnect(self, close_code):
        await print('websocket disconnected',close_code)