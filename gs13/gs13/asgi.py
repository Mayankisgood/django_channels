import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs3.settings")
from channels.routing import ProtocolTypeRouter,URLRouter
# application = get_asgi_application()
import app.routing
# from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        app.routing.web_socket_urlpatterns
    )
})