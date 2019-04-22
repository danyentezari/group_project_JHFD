
from django.db.models import Count
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView, View

from .forms import SortingForm

def people(request):
    return render(request, 'tutorial/people.html', {'people': Person.objects.all()})


class SortingView(TemplateView):

    template_name = 'exampleapp/itworks.html'

    # def get(self, request, *args, **kwargs):

    #     form = SortingForm()

    #     context = {
    #         "form": form
    #     }
    #     return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        form = SortingForm(request.POST)

        context = {
            "people": form.objects.all()
        }

        print(context)

        return self.render_to_response(context)