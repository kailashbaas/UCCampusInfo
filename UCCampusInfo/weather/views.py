from django.shortcuts import render

from . import forecast
from .models import HourForecast

def index(request):
    # get city from user settings (user may come from request)
    context = {
        'hourly_forecast': HourForecast.objects.all(),
    }
    return render(request, 'weather/index.html', context)
