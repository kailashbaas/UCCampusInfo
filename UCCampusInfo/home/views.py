from django.shortcuts import render

from weather.models import HourForecast
from menus.models import Menu

def home(request):
    context = {
        'hourly_forecast': HourForecast.objects.all(),
        'menus': Menu.objects.all(),
    }
    return render(request, 'home/home.html', context)
