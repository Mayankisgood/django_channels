from django.urls import path

from .import consumers

web_socket_urlpatterns =[          
    path('ws/sc/<str:groupkaname>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/asc/<str:groupkaname>/',consumers.MyAsyncConsumer.as_asgi()),
    ]