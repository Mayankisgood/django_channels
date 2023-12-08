from channels.consumer import SyncConsumer,AsyncConsumer

from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect ho gya',event)
        # ye default channel layer provide karega...
        print('channel layer ...',self.channel_layer)
        # get channel name
        print('channel name ...',self.channel_name)
        
        async_to_sync (self.channel_layer.group_add)('programmers',self.channel_name)
        
        # ye sabhi method async hote hai so pehle inhe sync mein change karna hoga
        
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
            print("web_socket ..receive",event)
            print("message is received from client",event["text"])
            print("type of message" ,type(event["text"]))
            # server client ko bhejat hai ye ---
            # ye frontend mein --  ws.onmessage =  function (event){
            #     console.log('message receive from server',event)
            # } event mein str(i) show hoga
            # for i in range(10):
            #     self.send({
            #         'type':'websocket.send',    
            #         'text':json.dumps({"count":i})
            #     })
            #     sleep(1)
            async_to_sync (self.channel_layer.group_send)('programmers',{
                'type': 'chat.message',
                'message':event['text']  
            })
            # chat.message ke liye handler banna hoga jo ki chat_message se hoga "." ki jagah "_"
    # is se msg client ko bhej diya
    def chat_message(self,event):
        print('event......',event)
        print('actual_data..',event['message'])
        print('type of actual_data..',type(event['message']))
        self.send(
            {
                'type':'websocket.send',
                'text':event['message']
            }
        )
                    
            
    def websocket_disconnect(self,event):
            print("websocket_disconnect",event)
            
            async_to_sync (self.channel_layer.group_discard)('programmers',self.channel_name)
            #  took too long to shut down and was killed. ye na aaye iske liye
            raise StopConsumer()
        
# async mein bhi same hoga bus  async_to_sync ki jarurat nhi hogi
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect',event)
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self,event):
        print("web_socket ..receive",event)
        for i in range(30):
            await  self.send({
            'type':'websocket.send',    
            'text': str(i)
             })
            await asyncio.sleep(1)
            
    async def websocket_disconnect(self,event):
        print("websocket_disconnect",event)
        raise StopConsumer()