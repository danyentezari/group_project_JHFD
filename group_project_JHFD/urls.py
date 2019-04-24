from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

import django_js_reverse.views

from group_project_JHFD import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),

    url(r'^$', views.dashboard_main, name='dashboard'),
    url(r'tester/', views.tester_main, name='tester_main'),
    url(r'tester1/', views.tester1_main, name='tester1_main'),
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
