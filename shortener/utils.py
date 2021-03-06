import secrets
import string

from django.conf import settings

from .models import Shortcut


def generate_shortcut(lenght=settings.SHORTCUT_LENGHT):
    alphabet = string.ascii_letters + string.digits
    link = "".join(secrets.choice(alphabet) for _ in range(lenght))
    return link


def get_link():
    try:
        shortcut = generate_shortcut()
        if Shortcut.objects.filter(link=shortcut).exists():
            return get_link()
        return shortcut
    except RecursionError:
        raise
