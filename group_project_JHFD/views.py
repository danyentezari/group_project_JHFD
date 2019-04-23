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

from .forms import SortingForm


def dashboard_main(request):

    print("context 123132")
    
    context = {
    }

    print(context)

    template = HttpResponse(loader.get_template('exampleapp/itworks.html').render(context=context, request=request))

    return template
         
def tester_main(request):
    
    form = SortingForm()

    print("context")
    
    context = {
            "form": form
        }

    print(context)

    template = HttpResponse(form)
    #template = HttpResponse(loader.get_template('exampleapp/searching.html').render(context=context, request=request))

    #return render_to_response('template.html', {'dictionary': my_dictionary}, context_instance=RequestContext(request)) 


    return template