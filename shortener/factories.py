import factory
from factory.fuzzy import FuzzyText
from django.conf import settings
from .models import Shortcut


class ShortcutFactory(factory.DjangoModelFactory):
    """Faktoria do obiektu Shortcut."""

    url = factory.Sequence(lambda n: f'{settings.BASE_URL}/%s' % n)
    #link = factory.Sequence(lambda n: 'john%s' % n)
    #link = FuzzyText(length=settings.SHORTCUT_LENGHT)
    link = factory.Faker('link', length=settings.SHORTCUT_LENGHT)
    #url = factory.Faker('url')

    class Meta:
        model = Shortcut
