from django.db.models import Count
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView, View

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

import json

from .forms import LoadData, main, click_SortDBpoint, click_SortDBalpha

def dashboard_main(request):
    context = {}
    template = HttpResponse(loader.get_template('exampleapp/itworks.html').render(context=context, request=request))
    return template 
         
def load_main(request):
    
    form = LoadData()
    context = {
            "formGold": form[0]['newArrayGold'],
            "formSilver": form[0]['newArraySilver'],
            "formPlatinum": form[0]['newArrayPlatinum'],
            "sortType" : "Initial Loaded data"
        }
    template = HttpResponse(loader.get_template('exampleapp/Sorting.html').render(context=context, request=request))
    return template

def merge_sort(request):

    form = click_SortDBalpha()

    print(form[0]['newArrayGold'])

    context = {
            "formGold": form[0]['newArrayGold'],
            "formSilver": form[0]['newArraySilver'],
            "formPlatinum": form[0]['newArrayPlatinum'],
            "sortType" : "Alphabetical sort"
        }
    template = HttpResponse(loader.get_template('exampleapp/Sorting.html').render(context=context, request=request))
    return template

def insertion_sort(request):
    
    form = click_SortDBpoint()
    context = {
             "formGold": form[0]['newArrayGold'],
            "formSilver": form[0]['newArraySilver'],
            "formPlatinum": form[0]['newArrayPlatinum'],
            "sortType" : "Point sort"
        }
    template = HttpResponse(loader.get_template('exampleapp/Sorting.html').render(context=context, request=request))
    return template

def Search(request):
    
    print(request.body)

    b = json.loads(request.body)
    print(b['searchValue'])

    form = main(b['searchValue'])
    context = {
            "form": form,
            "sortType" : "Hash-Based Search"
        }
    #template = HttpResponse(form)
    template = HttpResponse(loader.get_template('exampleapp/searching.html').render(context=context, request=request))
    #return render_to_response('template.html', {'dictionary': my_dictionary}, context_instance=RequestContext(request)) 
    return template