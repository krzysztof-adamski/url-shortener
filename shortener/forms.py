from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _

from .models import Shortcut
from .utils import get_link


class ShortcutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["url"].widget.attrs["required"] = "required"
        self.fields["url"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "`http://...`  `https://...`",
                "pattern": _("https://.*|http://.*"),
                "width": "50%",
            }
        )

    class Meta:
        model = Shortcut
        fields = ("url",)

    def _update_css_class(self, css_class):
        css_classes = self.fields["url"].widget.attrs["class"]
        self.fields["url"].widget.attrs.update(
            {"class": f"{css_classes} {css_class}"}
        )

    def clean_url(self):
        cleaned_data = super(ShortcutForm, self).clean()
        url = cleaned_data.get("url")
        validate_url = URLValidator()
        try:
            validate_url(url)
        except ValidationError:
            self._update_css_class("is-invalid")
        return url

    def save(self, commit=True):
        shortcut = super(ShortcutForm, self).save(commit=False)
        try:
            shortcut.link = get_link()
        except RecursionError:
            raise
        try:
            shortcut = Shortcut.objects.get(url=shortcut.url)
        except Shortcut.DoesNotExist:
            shortcut.save()
        self._update_css_class("is-valid")
        return shortcut
