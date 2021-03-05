import secrets
import string

from django.conf import settings

from .models import Shortcut


def generate_link():
    alphabet = string.ascii_letters + string.digits
    link = "".join(
        secrets.choice(alphabet) for _ in range(settings.SHORTCUT_LENGHT)
    )
    if Shortcut.objects.filter(link=link).exists():
        return generate_link()
    return link
