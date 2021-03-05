from django.shortcuts import get_object_or_404, redirect, render

from .forms import ShortcutForm
from .models import Shortcut


def index(request):
    shortcut = None
    if request.method == "POST":
        form = ShortcutForm(request.POST)
        if form.is_valid():
            shortcut = form.save()
    elif request.method == "GET":
        form = ShortcutForm()
    return render(
        request, "shortener/index.html", {"form": form, "shortcut": shortcut}
    )


def shortcut_redirect(request, link):
    shortcut = get_object_or_404(Shortcut, link=link)
    return redirect(shortcut.url)
