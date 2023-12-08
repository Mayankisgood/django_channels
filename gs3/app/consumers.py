from channels.consumer import SyncConsumer,AsyncConsumer

from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect ho gya',event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
            print("web_socket ..receive",event)
            print("message is received from client",event["text"])
            # server client ko bhejat hai ye ---
            # ye frontend mein --  ws.onmessage =  function (event){
            #     console.log('message receive from server',event)
            # } event mein str(i) show hoga
            for i in range(10):
                self.send({
                    'type':'websocket.send',    
                    'text':json.dumps({"count":i})
                })
                sleep(1)
    def websocket_disconnect(self,event):
            print("websocket_disconnect",event)
            #  took too long to shut down and was killed. ye na aaye iske liye
            raise StopConsumer()
            
# sync or async mein ye diff hai aap sync mein ,same url se connect to ho jaaoge 
# lekin msg send jab tak nhi hoga tab tak ki pehli request puri naa ho jaaye....           
# jab ki async mein aap kar sakte ho no need to wait to complete first request 
           
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
    