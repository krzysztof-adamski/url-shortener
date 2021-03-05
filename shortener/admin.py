from django.contrib import admin
from .models import Shortcut
from .forms import ShortcutForm


class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('url', 'link')
    list_display_links = ('url', 'link')
    readonly_fields = ('link',)
    form = ShortcutForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(ShortcutAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['url'].widget.attrs['style'] = 'width: 80%;'
        return form


admin.site.register(Shortcut, ShortcutAdmin)