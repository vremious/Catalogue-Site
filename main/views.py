from django.core.paginator import Paginator
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
    watches_filter = WatchFilter(request.GET, queryset=Watch.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умные часы'))
    testertime = TesterTime.objects.all().order_by('service')
    paginator = Paginator(watches_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = watches_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    return render(request, 'main/smart_watches.html', {'page_obj': page_obj,  'testertime': testertime, 'watches_filter': watches_filter, 'available':available, 'watches':watches, 'available_filter':available_filter, 'result':result, 'result1':result1,'final':final})


def smartphones(request):
    available = Available.objects.all().order_by('service')
    smartphones = Smartphone.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smartphones_filter = SmartphoneFilter(request.GET, queryset=Smartphone.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Смартфоны'))
    paginator = Paginator(smartphones_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smartphones_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'smartphones': smartphones, "smartphones_filter": smartphones_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/smartphones.html', context)


def smart_speaker(request):
    available = Available.objects.all().order_by('service')
    smart_speaker = SmartSpeaker.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smart_speaker_filter = SmartSpeakerFilter(request.GET, queryset=SmartSpeaker.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умные колонки'))
    paginator = Paginator(smart_speaker_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smart_speaker_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'smart_speakers': smart_speaker, "smart_speaker_filter": smart_speaker_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/smart_speaker.html', context)


def speaker(request):
    available = Available.objects.all().order_by('service')
    speaker = Speaker.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    speaker_filter = SpeakerFilter(request.GET, queryset=Speaker.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Аудиосистемы'))
    paginator = Paginator(speaker_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = speaker_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'speakers': speaker, "speaker_filter": speaker_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/speaker.html', context)

def routers(request):
    available = Available.objects.all().order_by('service')
    routers = Router.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    router_filter = RouterFilter(request.GET, queryset=Router.objects.filter(purpose='1', actual='Да').order_by('model__company__company', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Роутеры'))
    paginator = Paginator(router_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = router_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'routers': routers, "routers_filter": router_filter,
               "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/routers.html', context)



def routers_rent(request):
    available = Available.objects.all().order_by('service')
    routers = Router.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    router_filter = Router_RentFilter(request.GET,
                                 queryset=Router.objects.filter(purpose='2', actual='Да').order_by('model__company__company', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Модемы'))
    paginator = Paginator(router_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = router_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'routers': routers, "routers_filter": router_filter,
               "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/routers_rent.html', context)

def zala(request):
    available = Available.objects.all().order_by('service')
    zala = Zala.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    zala_filter = ZalaFilter(request.GET, queryset=Zala.objects.filter(actual='Да').order_by('type', 'model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Zala'))
    paginator = Paginator(zala_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = zala_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'zala': zala, 'zala_filter':zala_filter,'available_filter':available_filter, 'result':result, 'result1':result1,'final':final }
    return render(request, 'main/zala.html', context)

def smart_home(request):
    available = Available.objects.all().order_by('service')
    smart_home = SmartHome.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    smart_home_filter = SmartHomeFilter(request.GET, queryset=SmartHome.objects.filter(model__type='Умный Дом', actual='Да').order_by('type','model__model').distinct())
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Умный Дом'))
    paginator = Paginator(smart_home_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = smart_home_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'smart_home': smart_home, 'smart_home_filter':smart_home_filter,'available_filter':available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/smart_home.html', context)

def tv(request):
    available = Available.objects.all().order_by('service')
    tv = Tv.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    tv_filter = TVFilter(request.GET, queryset=Tv.objects.filter(actual='Да').order_by('model__company__company','size','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Телевизоры'))
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = tv_filter.qs.values('model').distinct().order_by('model')
    paginator = Paginator(tv_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj':page_obj, 'testertime': testertime, 'available':available, 'tv':tv, "tv_filter":tv_filter, "available_filter":available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/tv.html', context)

def notebooks(request):
    available = Available.objects.all().order_by('service')
    notebook = Notebook.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    notebook_filter = NotebookFilter(request.GET, queryset=Notebook.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    q1 = Available.objects.filter(model__type__contains='Ноутбуки')
    q2 = Available.objects.filter(model__type__contains="Компьютеры")
    available_filter = AvailableFilter(request.GET, queryset=q1|q2)
    paginator = Paginator(notebook_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = notebook_filter.qs.values('model').distinct().order_by('model')

    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'notebook': notebook, "notebook_filter": notebook_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/notebooks.html', context)

def pads(request):
    available = Available.objects.all().order_by('service')
    pads = Pad.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    pads_filter = PadFilter(request.GET, queryset=Pad.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Планшеты'))
    paginator = Paginator(pads_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = pads_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'pads': pads, "pads_filter": pads_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/pads.html', context)

def scooters(request):
    available = Available.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Электросамокаты'))
    scooters_filter = ScooterFilter(request.GET, queryset=Scooter.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    scooters = Scooter.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    paginator = Paginator(scooters_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = scooters_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'scooters': scooters, 'available_filter':available_filter, 'scooters_filter':scooters_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/scooters.html', context )


def bikes(request):
    available = Available.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Электровелосипеды'))
    bike_filter = BikeFilter(request.GET, queryset=Bikes.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    bikes = Bikes.objects.all
    testertime = TesterTime.objects.all().order_by('service')
    paginator = Paginator(bike_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = bike_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'bikes': bikes, 'available_filter':available_filter, 'bike_filter':bike_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/electrobike.html', context )


def robovacum(request):
    available = Available.objects.all().order_by('service')
    q1 = Available.objects.filter(model__type__contains='ылесос')
    q2 = Available.objects.filter(model__type__contains='окон')
    available_filter = AvailableFilter(request.GET, queryset=q1|q2)
    testertime = TesterTime.objects.all().order_by('service')
    vacuum = Vacuum.objects.all
    vacuum_filter = VacuumFilter(request.GET, queryset=Vacuum.objects.filter(actual='Да').order_by('model__type', 'model__company__company','model__model'))
    paginator = Paginator(vacuum_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = vacuum_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'vacuum': vacuum, 'available_filter': available_filter, 'vacuum_filter':vacuum_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/robovacum.html', context)


def coffee(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    coffee = Coffee.objects.all
    coffee_filter = CoffeeFilter(request.GET, queryset=Coffee.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type__icontains='Кофе'))
    paginator = Paginator(coffee_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = coffee_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'coffee': coffee, "coffee_filter": coffee_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}

    return render(request, 'main/coffee.html', context)


def conditioners(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Кондиционеры'))
    conditioners = Conditioner.objects.all
    conditioners_filter = ConditionerFilter(request.GET, queryset=Conditioner.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    paginator = Paginator(conditioners_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = conditioners_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'conditioners': conditioners, 'available_filter': available_filter,
                'conditioners_filter': conditioners_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/conditioners.html',  context)


def other(request):
    available = Available.objects.all().order_by('service')
    testertime = TesterTime.objects.all().order_by('service')
    other = Other.objects.all
    other_filter = OtherFilter(request.GET, queryset=Other.objects.filter(actual='Да').order_by('model__model'))
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type='Прочее оборудование'))
    paginator = Paginator(other_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = other_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'other': other, 'other_filter': other_filter, 'available_filter': available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/other.html', context)

def console(request):
    available = Available.objects.all().order_by('service')
    available_filter = AvailableFilter(request.GET, queryset=Available.objects.filter(model__type__contains='Игровые приставки'))
    testertime = TesterTime.objects.all().order_by('service')
    console = Console.objects.all
    console_filter = ConsoleFilter(request.GET, queryset=Console.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    paginator = Paginator(console_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = console_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'console': console, 'available_filter': available_filter, 'console_filter':console_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/console.html', context)


def cooking(request):
    available = Available.objects.all().order_by('service')
    q1 = Available.objects.filter(model__type__contains='Электрогрили')
    q2 = Available.objects.filter(model__type__contains='Сушилки')
    q3 = Available.objects.filter(model__type__contains='Соковыжималки')
    available_filter = AvailableFilter(request.GET, queryset=q1|q2|q3)
    testertime = TesterTime.objects.all().order_by('service')
    cooking = Cooking.objects.all
    cooking_filter = CookingFilter(request.GET, queryset=Cooking.objects.filter(actual='Да').order_by('model__company__company','model__model'))
    paginator = Paginator(cooking_filter.qs, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = available_filter.qs.values('model').distinct().order_by('model')
    result1 = cooking_filter.qs.values('model').distinct().order_by('model')
    final = True
    for i in result1:
        if i in result:
            final = False
    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'cooking': cooking, 'available_filter': available_filter, 'cooking_filter':cooking_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/cooking.html', context)


def upu2(request):
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
    paginator = Paginator(pads_filter.qs, 12) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'testertime': testertime, 'available': available, 'pads': pads, "pads_filter": pads_filter, "available_filter": available_filter, 'result':result, 'result1':result1,'final':final}
    return render(request, 'main/upu2.html', context)


def upu3(request):
    return render(request, 'main/upu3.html')


def upu4(request):
    return render(request, 'main/upu4.html')


def upu5(request):
    return render(request, 'main/upu5.html')



