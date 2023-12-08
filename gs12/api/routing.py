from django.urls import path

from .import consumers

web_socket_urlpatterns =[          
    path('ws/sc/',consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/asc/',consumers.MyAsyncWebsocketConsumer.as_asgi()),
    ]