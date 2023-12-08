import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs3.settings")
from channels.routing import ProtocolTypeRouter,URLRouter
# application = get_asgi_application()
import api.routing
# from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        api.routing.web_socket_urlpatterns
    )
})