import os
from django.core.wsgi import get_wsgi_application

env = os.getenv("ENV", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"blogweb.settings.{env}")

application = get_wsgi_application()
