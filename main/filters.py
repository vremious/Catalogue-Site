import django_filters
from django.forms import TextInput
from django_filters import *
from .models import *


# from .views import MainPage, CategoryPage

# def defaultfilter(q):
#     q1 = Company.objects.filter(models__cooking__in=q.objects.values('id'))
#     model__company = ModelChoiceFilter(label='Производитель',queryset=q1.distinct(), empty_label=('Все'))
#
#     q2 = Type.objects.filter(models__cooking__in=q.objects.values('id'))
#     model__type_fk = ModelChoiceFilter(label='Тип устройства',queryset=q2.distinct(), empty_label=('Все'))
#
#     model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
#                        widget=TextInput(
#                            attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
#                        )
#                        )
#
#     return model__company


class Filter(django_filters.FilterSet):
    # q1 = Models.objects.filter(company_id__in=1, actual='Да')
    # model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    # q1 = Available.objects.filter(model__model=model)
    # available = ModelChoiceFilter(queryset=q1)

    # class Meta:
    #     model = Models
    #     fields = {
    #         'company':['exact'],
    #         "model": ['icontains']
    #     }


class RouterFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__router__in=Router.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель',
                                       queryset=q1.exclude(models__router__purpose='2').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class Router_RentFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__router__in=Router.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель',
                                       queryset=q1.exclude(models__router__purpose='1').distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    type = ChoiceFilter(label='Тип модема', choices=(
        ('ADSL', 'ADSL'),
        ('VDSL', 'VDSL'),
        ('PON', 'PON')))
    wifi_freq = ChoiceFilter(label='Наличие и диапазон Wi-Fi', choices=(
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
        fields = {'type', "model"}


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
    q1 = Company.objects.filter(models__in=Models.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class SmartphoneFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__smartphone__in=Smartphone.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class PadFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__pad__in=Pad.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class NotebookFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__notebook__in=Notebook.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    q2 = Type.objects.filter(models__notebook__in=Notebook.objects.values('id'))
    model__type_fk = ModelChoiceFilter(label='Тип устройства', queryset=q2.distinct(), empty_label=('Все'))


class SmartSpeakerFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__smartspeaker__in=SmartSpeaker.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class SpeakerFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__speaker__in=Speaker.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class VacuumFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__vacuum__in=Vacuum.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))

    q2 = Type.objects.filter(models__vacuum__in=Vacuum.objects.values('id'))
    model__type_fk = ModelChoiceFilter(label='Тип устройства', queryset=q2.distinct(), empty_label=('Все'))

    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class ScooterFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__scooter__in=Scooter.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class BikeFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__bikes__in=Bikes.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class ConditionerFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__conditioner__in=Conditioner.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class AvailableFilter(django_filters.FilterSet):
    class Meta:
        model = Available
        fields = {'service', 'available', 'model__model', 'model__company__company'}


class TVFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__tv__in=Tv.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))
    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
    size = CharFilter(label='Диагональ', lookup_expr='icontains', widget=TextInput(
        attrs={'style': 'width: 100%', 'placeholder': 'Введите размер'}
    ))


class CoffeeFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__coffee__in=Coffee.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))

    q2 = Type.objects.filter(models__coffee__in=Coffee.objects.values('id'))
    model__type_fk = ModelChoiceFilter(label='Тип устройства', queryset=q2.distinct(), empty_label=('Все'))

    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )

    capucinator = ChoiceFilter(empty_label=('Все'), choices=(
        ('Ручной', 'Ручной'),
        ('Автоматичесий', 'Автоматичесий')))


class ConsoleFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__console__in=Console.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))

    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )


class CookingFilter(django_filters.FilterSet):
    q1 = Company.objects.filter(models__cooking__in=Cooking.objects.values('id'))
    model__company = ModelChoiceFilter(label='Производитель', queryset=q1.distinct(), empty_label=('Все'))

    q2 = Type.objects.filter(models__cooking__in=Cooking.objects.values('id'))
    model__type_fk = ModelChoiceFilter(label='Тип устройства', queryset=q2.distinct(), empty_label=('Все'))

    model = CharFilter(field_name='model__model', label='Поиск по модели', lookup_expr='icontains',
                       widget=TextInput(
                           attrs={'style': 'width: 100%', 'placeholder': 'Введите модель'}
                       )
                       )
