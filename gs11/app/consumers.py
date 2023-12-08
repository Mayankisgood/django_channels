from channels.consumer import SyncConsumer,AsyncConsumer

from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from .models import *
from channels.db import database_sync_to_async

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect ho gya',event)
        # ye default channel layer provide karega...
        print('channel layer ...',self.channel_layer)
        # get channel name
        print('channel name ...',self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group__name",self.group_name)
        
        async_to_sync (self.channel_layer.group_add)(self.group_name,self.channel_name)
        
        # ye sabhi method async hote hai so pehle inhe sync mein change karna hoga
        
        self.send({
            'type':'websocket.accept'
        })
    # def websocket_receive(self,event):
    #         print("web_socket ..receive",event)
    #         print("message is received from client",event["text"])
    #         print("type of message" ,type(event["text"]))
            
    #         data = json.loads(event['text'])
    #         print("data",data)
    #         print("type of data", type(data))
    #         print("chat message", data['msg'])
    #         print(self.scope['user'])
    #         group = Group.objects.get(name = self.group_name)
    #         if self.scope['user'].is_authenticated:
            
    #             # crate chat object
    #             chat = Chat(
    #                 content = data['msg'],
    #                 group = group
    #                 )
    #             chat.save()
    #             async_to_sync (self.channel_layer.group_send)(self.group_name,{
    #                 'type': 'chat.message',
    #                 'message':event['text']  
    #             })
    #         else:
    #             self.send({
    #                 'type':'websocket.send',
    #                 'text':json.dumps({"msg":"login Required"})
    #             })
    
    
    # showing user
    def websocket_receive(self,event):
            print("web_socket ..receive",event)
            print("message is received from client",event["text"])
            print("type of message" ,type(event["text"]))
            
            data = json.loads(event['text'])
            print("data",data)
            print("type of data", type(data))
            print("chat message", data['msg'])
            print(self.scope['user'])
            group = Group.objects.get(name = self.group_name)
            if self.scope['user'].is_authenticated:
            
                # crate chat object
                chat = Chat(
                    content = data['msg'],
                    group = group
                    )
                chat.save()
                data['user'] = self.scope['user'].username
                print("completed data",data)
                print("type of completed data",type(data))
                async_to_sync (self.channel_layer.group_send)(self.group_name,{
                    'type': 'chat.message',
                    'message':json.dumps(data)
                })
            else:
                self.send({
                    'type':'websocket.send',
                    'text':json.dumps({"msg":"login Required",
                    'user':'unknown'})
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
            
            async_to_sync (self.channel_layer.group_discard)(self.group_name,self.channel_name)
            #  took too long to shut down and was killed. ye na aaye iske liye
            raise StopConsumer()
        
# async mein bhi same hoga bus  async_to_sync ki jarurat nhi hogi
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect',event)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group__name",self.group_name)
        await (self.channel_layer.group_add)(self.group_name,self.channel_name)
        
        
        
        await self.send({
            'type':'websocket.accept'
        })
        
    async def chat_message(self, event):
        message = event['message']
        await self.send({
            'type': 'websocket.send',
            'text': message,
        })
        
    # async def websocket_receive(self,event):
    #     print("web_socket ..receive",event)
    #     print("message is received from client",event["text"])
    #     print("type of message" ,type(event["text"]))
        
    #     data = json.loads(event['text'])
    #     print("data",data)
    #     print("type of data", type(data))
    #     print("chat message", data['msg'])
    #     group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
        
    #     if self.scope['user'].is_authenticated:

    #         # crate chat object
    #         chat = Chat(
    #             content = data['msg'],
    #             group = group
    #             )
    #         await database_sync_to_async(chat.save)()
            
    #         await self.channel_layer.group_send(
    #             self.group_name,
    #             {
    #                 'type': 'chat.message',
    #                 'message':event['text']  
    #             })
    #     else:
    #         await self.send({
    #             'type':'websocket.send',
    #             'text':json.dumps({"msg":"login Required"})
    #         })
    
    # when showing user
    async def websocket_receive(self,event):
        print("web_socket ..receive",event)
        print("message is received from client",event["text"])
        print("type of message" ,type(event["text"]))
        
        data = json.loads(event['text'])
        print("data",data)
        print("type of data", type(data))
        print("chat message", data['msg'])
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
        
        if self.scope['user'].is_authenticated:

            # crate chat object
            chat = Chat(
                content = data['msg'],
                group = group
                )
            await database_sync_to_async(chat.save)()
            
            data['user'] = self.scope['user'].username
            print("completed data",data)
            print("type of completed data",type(data))
            
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message':json.dumps(data)
                })
        else:
            await self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"login Required",'user':'guest'})
            })
        
            
    async def websocket_disconnect(self,event):
        print("websocket_disconnect",event)
        raise StopConsumer()