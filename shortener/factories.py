from django.conf import settings

import factory
from factory.fuzzy import FuzzyText

from .models import Shortcut


class ShortcutFactory(factory.DjangoModelFactory):
    """Faktoria do obiektu Shortcut."""

    url = factory.Faker("url")
    link = FuzzyText(length=settings.SHORTCUT_LENGHT)

    class Meta:
        model = Shortcut
