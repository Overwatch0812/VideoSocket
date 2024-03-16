
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'^ws/$', consumers.AsyncSocketConsumer.as_asgi()),
    # re_path(r'^ws/$', consumers.SyncAudioSocketConsumer.as_asgi()),
    re_path(r'^ws/$', consumers.SyncSocketConsumer.as_asgi()),
]
