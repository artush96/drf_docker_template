import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from apps.drivers.api.services import socket_location


class GetDriverLocationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.driver_id = self.scope['url_route']['kwargs']['driver_id']
        self.company_id = self.scope['url_route']['kwargs']['company_id']
        self.driver_group_name = 'driver_%s-%s' % (self.company_id, self.driver_id)

        # Join room group
        await self.channel_layer.group_add(
            self.driver_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.driver_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        location_data = text_data
        location_data_json = json.loads(location_data)
        location = {
            'latitude': location_data_json['latitude'],
            'longitude': location_data_json['longitude']
        }
        new_location = await self.create_or_update_location(location)
        data = {
            'company_id': self.company_id,
            'driver_id': self.driver_id,
            'location': new_location
        }
        # Send message to room group
        await self.channel_layer.group_send(
            self.driver_group_name,
            {
                'type': 'new_location',
                'data': data
            }
        )

    # Receive message from room group
    async def new_location(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': data
        }))

    @database_sync_to_async
    def create_or_update_location(self, location):
        socket_location(self, location)
        return location
