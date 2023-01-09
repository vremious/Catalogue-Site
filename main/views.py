from django.shortcuts import render
from django.db.models import Count
from .models import Good, State, Available, Notebook, Router, Pad, Watch, Scooter, Vacuum, Zala




def index(request):
    return render(request, 'main/index.html')

def routers(request):
    good = Available.objects.all
    routers = Router.objects.all
    return render(request, 'main/routers.html', {'good': good, 'routers': routers})

def routers_rent(request):
    available = Available.objects.all
    routers = Router.objects.all
    return render(request, 'main/routers_rent.html', {'available': available, 'routers': routers})

def zala(request):
    available = Available.objects.all
    zala = Zala.objects.all
    return render(request, 'main/zala.html', {'available': available, 'zala': zala})

def smart_home(request):
    return render(request, 'main/smart_home.html')

def tv(request):
    return render(request, 'main/tv.html')

def notebooks(request):
    available = Available.objects.all
    notebook = Notebook.objects.all
    return render(request, 'main/notebooks.html', {'notebook': notebook, 'available': available})

def pads(request):
    available = Available.objects.all
    pads = Pad.objects.all
    return render(request, 'main/pads.html', {'available': available, 'pads': pads})

def smart_watches(request):
    available = Available.objects.all
    watches = Watch.objects.all
    return render(request, 'main/smart_watches.html', {'available': available, 'watches': watches})

def scooters(request):
    available = Available.objects.all
    scooters= Scooter.objects.all
    return render(request, 'main/scooters.html', {'available': available, 'scooters': scooters})

def robovacum(request):
    available = Available.objects.all
    vacuum = Vacuum.objects.all
    return render(request, 'main/robovacum.html', {'available': available, 'vacuum': vacuum})

def coffee(request):
    return render(request, 'main/coffee.html')

def conditioners(request):
    return render(request, 'main/conditioners.html')

def other(request):
    return render(request, 'main/other.html')

def upu1(request):
    return render(request, 'main/routers_rent.html')

def upu2(request):
    return render(request, 'main/upu2.html')

def upu3(request):
    return render(request, 'main/upu3.html')

def upu4(request):
    return render(request, 'main/upu4.html')

def upu5(request):
    return render(request, 'main/upu5.html')


