from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django_plotly_dash.consumers import MessageConsumer
from channels.auth import AuthMiddlewareStack
from django.urls import path


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("ws/", MessageConsumer.as_asgi()),
            ])
        )
    ),
})