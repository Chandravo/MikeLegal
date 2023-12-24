"""
ASGI config for mikelegal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os
# from django.core.asgi import get_asgi_application
# django_asgi_app = get_asgi_application()
# # import django
# # django.setup()

# from channels.routing import ProtocolTypeRouter, URLRouter
# from app.routing import websocket_urlpatterns
# # from django.conf import settings
# # settings.config()


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikelegal.settings')

# # application = get_asgi_application()

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket':
#         URLRouter(
#             websocket_urlpatterns
#         )
    
# })


import os
import django
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikelegal.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    
})

# Use Django's logging configuration if available
# if settings.LOGGING_CONFIG:
#     from django.utils.log import configure_logging
#     configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)