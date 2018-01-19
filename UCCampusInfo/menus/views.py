from django.shortcuts import render

from . import menus
from .models import Menu

def index(request):
    context = {
        'menus': Menu.objects.all(),
    }

    return render(request, 'menus/index.html', context)
