import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from competitions.models import Submission,Competitions,Question
from .tasks import hello_world

class MyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("my consumer connected", event)
        chat_room = 'sameed_1'
        self.chat_room = chat_room
        print(self.channel_name,"channel name")
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            "type":"websocket.accept",
        }) 

    async def websocket_receive(self, event):
        print("recieve", event)
        data = event.get("text", None)
        if data is not None:
            loaded_dict_data = json.loads(data)
            my_dic = loaded_dict_data.get('message')
            print(my_dic,'my dict')
            submission = Submission.objects.filter(id=my_dic['sub_id']).first()
            print(submission,'sub')
            if loaded_dict_data.get('action')=='check':
                #file will be checked here
                hello_world()
                myResponse = {
                    'id': submission.id,
                    'verdict':'checking',
                }
                submission.verdict = 'checking'
                submission.save()
                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                        'type':'chat_message',
                        'text': json.dumps(myResponse)
                    }
            )

    async def websocket_disconnect(self, event):
        print("disconnected", event)
    
    async def chat_message(self,event):
        await self.send({
            'type':"websocket.send",
            'text':event['text']
        })





# class MyMessageConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("my message consumer connected", event)
#         await self.send({
#             "type":"websocket.accept",
#         })
#         await self.send({
#             'type':'websocket.send',
#             'text':'hello world from message url'
#         })

#     async def websocket_receive(self, event):
#         print("recieve", event)
        # myResponse = {
        #         'message':"hello message aayela hai",
        #     }
        # await self.channel_layer.group_send(
        #         self.chat_room,
        #         {
        #             'type':'chat_message',
        #             'text':json.dumps(myResponse)
        #         }
        #     )

#     async def websocket_disconnect(self, event):
#         print("disconnected", event)






# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected", event)
#         other_user = self.scope['url_route']['kwargs']['username']
#         me = self.scope['user']
#         print(other_user,me)
#         thread_obj = await self.get_thread(me,other_user)
#         print(thread_obj)
#         self.thread_obj = thread_obj
#         chat_room = f'thread_{thread_obj.id}'
#         self.chat_room = chat_room
#         # await asyncio.sleep(10)
#         await self.channel_layer.group_add(
#             chat_room,
#             self.channel_name
#         )
#         await self.send({
#             "type":"websocket.accept"
#         })
        

#     async def websocket_receive(self, event):
#         print("recieve", event)
#         front_text = event.get("text",None)
#         if front_text is not None:
#             loaded_dict_data = json.loads(front_text)
#             msg = loaded_dict_data.get('message')
#             user = self.scope['user']
#             username='default'
#             if user.is_authenticated:
#                 username = user.username
#             myResponse = {
#                 'message':msg,
#                 'username':username
#             }
#             await self.create_chat_message(user,msg)
#             await self.channel_layer.group_send(
#                 self.chat_room,
#                 {
#                     'type':'chat_message',
#                     'text':json.dumps(myResponse)
#                 }
#             )
#     async def chat_message(self,event):
#         await self.send({
#             'type':"websocket.send",
#             'text':event['text']
#         })

#     async def websocket_disconnect(self, event):
#         print("disconnected", event)

#     @database_sync_to_async
#     def get_thread(self,user,other_user):
#         return Thread.objects.get_or_new(user,other_user)[0]

#     @database_sync_to_async
#     def create_chat_message(self,me,msg):
#         thread_obj = self.thread_obj
#         return ChatMessage.objects.create(thread=thread_obj,user=me,message=msg)