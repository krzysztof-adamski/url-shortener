import unittest
from shortener.views import index, shortcut_redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
#from django.test import TestCase, RequestFactory
from shortener.models import Shortcut
from shortener.factories import ShortcutFactory


class IndexTests(unittest.TestCase):
    def setUp(self):
        import pdb; pdb.set_trace()
        self.shortcut = ShortcutFactory()
        self.shortcut.get_absolute_url.return_value = reverse('shortcut_detail', kwargs={'link': self.show.id})
