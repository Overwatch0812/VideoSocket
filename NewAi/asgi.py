import os
from django.core.asgi import get_asgi_application
from sockets.routing import websocket_urlpatterns

from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSocket.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
