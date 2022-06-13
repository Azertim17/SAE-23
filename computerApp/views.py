from django.shortcuts import get_object_or_404, render

# Create your views here

from django.shortcuts import render
from django.http import HttpResponse
from computerApp.models import Machine 
from computerApp.models import Personnel
from datetime import date, datetime
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


def index(request):
	machines = Machine.objects.all()
	personnels= Personnel.objects.all()

	context={
		'machines':machines,
		'personnels':personnels,
		
	}
	

	return render(request, 'templates/index.html', context)


def machine_list_view (request) :
	machines = Machine.objects.all ()
	context ={'machines': machines }
	return render (request,'machine_list.html',context)


def machine_detail_view (request , pk):
	machine = get_object_or_404 ( Machine, id=pk )
	context ={'machine': machine }
	return render (request,'machine_detail.html',context )


def personnel_list_view (request) :
	personnels = Personnel.objects.all ()
	context ={'personnels': personnels }
	return render (request,'personnel_list.html',context)


def personnel_detail_view (request , pk):
	personnel = get_object_or_404 ( Personnel, id=pk )
	context ={'personnel': personnel }
	return render (request,'personnel_detail.html',context )


class CalendarView(generic.ListView):
    model = Event
    template_name = 'maintenance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()