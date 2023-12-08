"""
ASGI config for gs2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs2.settings")
from channels.routing import ProtocolTypeRouter,URLRouter
# application = get_asgi_application()
import app.routing

application = ProtocolTypeRouter({
    'http':get_asgi_application,
    'websocket':URLRouter(
        app.routing.web_socket_urlpatterns
    )
})


# --ws://127.0.0.1:8000/ws/sc
# --wss://127.0.0.1:8000/ws/sc