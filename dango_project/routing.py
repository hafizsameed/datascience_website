from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, AllowedHostsOriginValidator
from competitions.consumers import MyConsumer

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                # url(r"^messages/(?P<username>[\w.@+-]+)/$",ChatConsumer),
                # url("kuchbhi/",MyConsumer),
                 url("",MyConsumer),
                 url('contests/<int:param1>/mysubmissions',MyConsumer),
                 url('contests/problem/<int:param1>/<int:param2>', MyConsumer),
                ]
            )
        )
    )
})
