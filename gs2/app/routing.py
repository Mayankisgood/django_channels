from django.urls import path

from .import consumers

web_socket_urlpatterns =[          
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    path('ws/asc/',consumers.MyAsyncConsumer.as_asgi()),
    ]
