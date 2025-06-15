import os
from django.core.asgi import get_asgi_application

env = os.getenv("ENV", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"blogweb.settings.{env}")

application = get_asgi_application()
