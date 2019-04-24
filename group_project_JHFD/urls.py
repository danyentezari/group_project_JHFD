from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

import django_js_reverse.views

from group_project_JHFD import views

#This is where the url routing is setup in python to call the various api endpoints
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),

    url(r'^$', views.dashboard_main, name='dashboard'),
    url(r'loadData/', views.load_main, name='load_main'),
    url(r'mergeSort/', views.merge_sort, name='merge_sort'),
    url(r'insertionSort/', views.insertion_sort, name='insertion_sort'),
    url(r'Search/', views.Search, name='Search'),
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
