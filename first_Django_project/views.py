__author__ = 'Administrator'
from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse('Hello World!')

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('meta.html', locals())

def my_homepage_view(request):
    return HttpResponse('Welcome To My Home--page!!')

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())

