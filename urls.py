from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from shortener import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(r'link', RedirectView.as_view(url='/link/')),
    path('<str:link>/', views.shortcut_redirect, name='shortcut_detail'),
]
urlpatterns += staticfiles_urlpatterns()
