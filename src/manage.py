import os
import sys


def main():
    env = os.getenv("ENV", "development")
    settings_module = f"blogweb.settings.{env}"

    try:
        __import__(settings_module)
    except ImportError as exc:
        raise ImportError(
            f"Unable to import settings '{settings_module}'. Make sure ENV is set to a valid settings file."
        ) from exc

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"blogweb.settings.{env}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
