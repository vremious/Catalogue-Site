from django.db.models import Q
from django.shortcuts import render
from .models import *
from .filters import *
# from django.views.generic.base import View
# from django.views.generic.list import ListView

from itertools import chain



def index(request):
    testertime = TesterTime.objects.all().order_by('service')
    context = {'testertime': testertime}
    return render(request, 'main/index.html', context)

def smart_watches_def(request):
    available = Available.objects.all().order_by('service')
    watches = Watch.objects.all
    watches_filter = WatchFilter(request.GET, queryset=Watch.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умные часы'))
    testertime = TesterTime.objects.all().order_by('service')
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = watches_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    return render(request, 'main/smart_watches.html', { 'testertime': testertime, 'watches_filter': watches_filter, 'available':available, 'watches':watches, 'available_filter':available_filter, 'result':result, 'result1':result1,'final':final})


def smartphones(request):
    available = Available.objects.all().order_by('service')
    smartphones = Smartphone.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smartphones_filter = SmartphoneFilter(request.GET, queryset=Smartphone.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Смартфоны'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smartphones_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'smartphones': smartphones, "smartphones_filter": smartphones_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/smartphones.html', context)


def smart_speaker(request):
    available = Available.objects.all().order_by('service')
    smart_speaker = SmartSpeaker.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smart_speaker_filter = SmartSpeakerFilter(request.GET, queryset=SmartSpeaker.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умные колонки'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smart_speaker_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'smart_speakers': smart_speaker, "smart_speaker_filter": smart_speaker_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/smart_speaker.html', context)


def speaker(request):
    available = Available.objects.all().order_by('service')
    speaker = Speaker.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    speaker_filter = SpeakerFilter(request.GET, queryset=Speaker.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Аудиосистемы'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = speaker_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'speakers': speaker, "speaker_filter": speaker_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/speaker.html', context)

def routers(request):
    available = Available.objects.all().order_by('service')
    routers = Router.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    router_filter = RouterFilter(request.GET, queryset=Router.objects.filter(purpose='1').order_by('model__company__company', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Роутеры'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = router_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'routers': routers, "routers_filter": router_filter,
               "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/routers.html', context)



def routers_rent(request):
    available = Available.objects.all().order_by('service')
    routers = Router.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    router_filter = Router_RentFilter(request.GET,
                                 queryset=Router.objects.filter(purpose='2').order_by('model__company__company', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Модемы'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = router_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'routers': routers, "routers_filter": router_filter,
               "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/routers_rent.html', context)

def zala(request):
    available = Available.objects.all().order_by('service')
    zala = Zala.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    zala_filter = ZalaFilter(request.GET, queryset=Zala.objects.all().order_by('type', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Zala'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = zala_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'zala': zala, 'zala_filter':zala_filter,'available_filter':available_filter, 'result':result, 'result1':result1,'final':final }
    return render(request, 'main/zala.html', context)

def smart_home(request):
    available = Available.objects.all().order_by('service')
    smart_home = SmartHome.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smart_home_filter = SmartHomeFilter(request.GET, queryset=SmartHome.objects.filter(model__type='Умный Дом').order_by('type','model__model').distinct())
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умный Дом'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smart_home_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'smart_home': smart_home, 'smart_home_filter':smart_home_filter,'available_filter':available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/smart_home.html', context)

def tv(request):
    available = Available.objects.all().order_by('service')
    tv = Tv.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    tv_filter = TVFilter(request.GET, queryset=Tv.objects.all().order_by('model__company__company','size','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Телевизоры'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = tv_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available':available, 'tv':tv, "tv_filter":tv_filter, "available_filter":available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/tv.html', context)

def notebooks(request):
    available = Available.objects.all().order_by('service')
    notebook = Notebook.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    notebook_filter = NotebookFilter(request.GET, queryset=Notebook.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Ноутбуки'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = notebook_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'notebook': notebook, "notebook_filter": notebook_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/notebooks.html', context)

def pads(request):
    available = Available.objects.all().order_by('service')
    pads = Pad.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    pads_filter = PadFilter(request.GET, queryset=Pad.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Планшеты'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = pads_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'pads': pads, "pads_filter": pads_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/pads.html', context)

def scooters(request):
    available = Available.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Электросамокаты'))
    scooters_filter = ScooterFilter(request.GET, queryset=Scooter.objects.all().order_by('model__company__company','model__model'))
    scooters = Scooter.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = scooters_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'scooters': scooters, 'available_filter':available_filter, 'scooters_filter':scooters_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/scooters.html', context )


def robovacum(request):
    available = Available.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Роботы пылесосы'))
    testertime = TesterTime.objects.all().order_by('service')
    vacuum = Vacuum.objects.all
    vacuum_filter = VacuumFilter(request.GET, queryset=Vacuum.objects.all().order_by('model__company__company','model__model'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = vacuum_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'vacuum': vacuum, 'available_filter': available_filter, 'vacuum_filter':vacuum_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/robovacum.html', context)


def coffee(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    coffee = Coffee.objects.all
    coffee_filter = CoffeeFilter(request.GET, queryset=Coffee.objects.all().order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Кофе-машины'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = coffee_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'coffee': coffee, "coffee_filter": coffee_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/coffee.html', context)


def conditioners(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Кондиционеры'))
    conditioners = Conditioner.objects.all
    conditioners_filter = ConditionerFilter(request.GET, queryset=Conditioner.objects.all().order_by('model__company__company','model__model'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = conditioners_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'conditioners': conditioners, 'available_filter': available_filter,
                'conditioners_filter': conditioners_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/conditioners.html',  context)


def other(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    other = Other.objects.all
    other_filter = OtherFilter(request.GET, queryset=Other.objects.all().order_by('model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Прочее оборудование'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = other_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'testertime': testertime, 'available': available, 'other': other, 'other_filter': other_filter, 'available_filter': available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/other.html', context)



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



