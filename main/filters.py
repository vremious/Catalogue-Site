import django_filters
from django.forms import TextInput
from django_filters import *
from .models import *



class RouterFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Роутер').exclude(models__router__purpose='2').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class Router_RentFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Модем').exclude(models__router__purpose='1').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )
    type= ChoiceFilter(label='Тип модема', choices= (
        ('ADSL', 'ADSL'),
        ('VDSL', 'VDSL'),
        ('PON', 'PON')))
    wifi_freq = ChoiceFilter(label= 'Наличие и диапазон Wi-Fi', choices =(
        ('2,4', '2,4 ГГц'),
        ('2,4/5', '2,4/5 ГГц'),
        ('-', 'Нет')))




class ZalaFilter(django_filters.FilterSet):
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    class Meta:
        model = Zala
        fields = {'type',"model"}

class SmartHomeFilter(django_filters.FilterSet):
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    type = ChoiceFilter(empty_label=('Все'), choices=(
        ('Комплект', "Комплект"),
        ("Компонент", "Компонент")
    ))


class OtherFilter(django_filters.FilterSet):
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    class Meta:
        model = Other
        fields = {"model"}


class WatchFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Умные часы').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class SmartphoneFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Смартфоны').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class PadFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Планшеты').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )



class NotebookFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Ноутбуки').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class SmartSpeakerFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Умные колонки').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )


class SpeakerFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Аудиосистемы').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )


class VacuumFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__type__contains='ылесос')
    q2 = Company.objects.filter(models__type__contains='окон')
    model__company = ModelChoiceFilter(label='Производитель', queryset=(q1|q2).distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )
    type = ChoiceFilter(empty_label=('Все'), label='Тип устройства', choices=(
        ('Робот', "Робот пылесос"),
        ("Вертикальный", "Вертикальный пылесос"),
	    ('Мойщик окон', 'Мойщик окон')
    )
                       )


class ScooterFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Электросамокаты').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class BikeFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Электровелосипеды').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )


class ConditionerFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Кондиционеры').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )



class AvailableFilter(django_filters.FilterSet):
    available = ChoiceFilter(label='Наличие', choices=(('+','Есть' ),('-','Нет')), empty_label='Все')


    class Meta:
        model = Available
        fields = {'service', 'available'}



class TVFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(queryset=Company.objects.filter(models__type__contains='Телевизор').distinct(), empty_label=('Все'), label='Производитель')
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )
    size = CharFilter(label='Диагональ', lookup_expr='icontains', widget=TextInput(
        attrs={'style': 'width: 100%',  'placeholder':'Введите размер'}
    ))


class CoffeeFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(queryset=Company.objects.filter(models__type__contains='Кофе-машины').distinct(), empty_label=('Все'), label='Производитель')
    mod = ChoiceFilter(empty_label=('Все'), choices=(
        ('Кофеварка', "Кофеварка"),
        ("Кофемашина", "Кофемашина")
    )
                       )
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

    capucinator = ChoiceFilter(empty_label=('Все'), choices=(
        ('Ручной', 'Ручной'),
        ('Автоматичесий', 'Автоматичесий')))
    # class Meta:
    #     model = Coffee
    #     fields = {'capucinator',}

class ConsoleFilter(django_filters.FilterSet):
    model__company = ModelChoiceFilter(label='Производитель', queryset=Company.objects.filter(models__type__contains='Игровые приставки').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )

class CookingFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__type__contains='грили')
    q2 = Company.objects.filter(models__type__contains='Соковыжималки')
    q3 = Company.objects.filter(models__type__contains='Сушилки')
    model__company = ModelChoiceFilter(label='Производитель', queryset=(q1|q2|q3).distinct(), empty_label=('Все'))
    type = ChoiceFilter(empty_label=('Все'), choices=(
        ('Электрогриль', 'Электрогриль'),
        ('Соковыжималка', 'Соковыжималка'),
        ('Сушилка', 'Сушилка'),
    )
                       )
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%',  'placeholder':'Введите модель'}
                       )
                       )