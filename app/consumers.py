from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import ChatRoom, Message
from channels.db import database_sync_to_async
from django.conf import settings
import os 
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.send_new_user_notification()
        
        await self.accept()
        
    
    async def send_new_user_notification(self):
        # Send a notification message when a new user connects
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'new_user_notification',
                # 'username': self.scope['user'].username,
            }
        )
        
    async def new_user_notification(self, event):
        # username = event['username']
        message = f'A new user has joined the chat!'
        await self.send(text_data=json.dumps({
            'class': 'notification',
            'message': message,
        }))
        
    async def send_left_user_notification(self):
        # Send a notification message when a new user connects
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'left_user_notification',
                # 'username': self.scope['user'].username,
            }
        )
        
    async def left_user_notification(self, event):
        # username = event['username']
        message = f'A user has left the chat!'
        await self.send(text_data=json.dumps({
            'class': 'notification',
            'message': message,
        }))
    
    async def disconnect(self, close_code):
        await self.send_left_user_notification()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    @database_sync_to_async
    def add_message(self, room_name, message):
        try:
            room = ChatRoom.objects.filter(key=room_name).first()
            if room is None:
                room = ChatRoom.objects.create(key=room_name)
                room.save()
            mess = Message.objects.create(room=room, message=message)
            mess.save()
            return True
        except Exception as e:
            print(e)
            return False
        
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # roomnanme = text_data_json['room_name']
        ok = await self.add_message(self.room_name, message)
        
        # username = text_data_json['username']
        tokens=word_tokenize(message)
        print(pos_tag(tokens))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'chatroom_message',
                'message' : message,
                # 'username' : username
            }
        )
        
    async def chatroom_message(self, event):
        message = event['message']
        # username = event['username']
        # NLTK_DATA_DIR = os.path.join(settings.BASE_DIR, 'nltk_data')
        
        await self.send(text_data=json.dumps({
            'class' : 'message',
            'message' : message,
            # 'username' : username
        }))  
        
    
