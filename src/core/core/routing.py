from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django_plotly_dash.consumers import MessageConsumer
from channels.auth import AuthMiddlewareStack
from django.urls import path, re_path
from django_plotly_dash.util import pipe_ws_endpoint_name


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                re_path(pipe_ws_endpoint_name(), MessageConsumer.as_asgi()),
            ])
        )
    ),
})