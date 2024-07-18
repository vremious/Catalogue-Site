from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, renderers, request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from .serializer import ModelsSerializer, CompanySerializer, TypeSerializer
from .models import *


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'company']


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'company']


class ModViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer
    renderer_classes = [JSONRenderer]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'model', 'company__company', 'type_fk__type']


class Homing(ListView):
    model = Filial
    template_name = "main/homing.html"


class MainPage(ListView):
    model = Models
    template_name = "main/category_detail.html"
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["testertime"] = TesterTime.objects.all().select_related('service').filter(
            service__filial__slug=self.kwargs['slug']
        ).order_by('service')
        context['typed'] = Available.objects.select_related('model__type_fk', 'model__type_fk__purpose',
                                                            'service__filial').filter(model__actual='Да').order_by(
            'model__type_fk_id', 'model__id')
        context['filial'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      quantity__gt=0, model__actual='Да').order_by(
            'model__type_fk_id', 'model__id')
        context['typed1'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      model__actual='Да').order_by(
            'model__type_fk')
        context['type'] = Type.objects.select_related('purpose')
        context['image'] = Models.objects.values_list('image', 'id').first()
        context['city'] = Filial.objects.select_related().filter(slug__exact=self.kwargs['slug'])[0]
        context['main_button'] = ''
        context['city17'] = Filial.objects.select_related().filter(
            filial__exact=context['city']).values_list('slug', flat=True)[0]
        return context


class CategoryPage(ListView):
    model = Models
    template_name = "main/upu4.html"
    context_object_name = 'models'

    def get_queryset(self):
        if self.request.GET.get('Company') or self.request.GET.get('Model') or self.request.GET.get('Service') \
                or self.request.GET.get('Available') or self.request.GET.get('Add_filter'):
            if self.request.GET.get('Add_filter'):
                qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                       'model__add_filter', 'model__add_filter_name').filter(
                    model__type_fk__slug=self.kwargs['cat_slug'], model__actual='Да',
                    model__company__company__icontains=self.request.GET.get('Company'),
                    model__model__icontains=self.request.GET.get('Model'),
                    service__service_centre__icontains=self.request.GET.get('Service'),
                    available__icontains=self.request.GET.get('Available'),
                    model__add_filter__value__icontains=self.request.GET.get('Add_filter'),
                    service__filial__slug=self.kwargs['slug']
                ).order_by(self.request.GET.get('sort', default='model__company__company'), 'model__model',
                           'service__service_centre', 'model__add_filter__value')
            else:
                qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                       'model__add_filter_name', 'model__add_filter').filter(
                    model__type_fk__slug=self.kwargs['cat_slug'], model__actual='Да',
                    model__company__company__icontains=self.request.GET.get('Company'),
                    model__model__icontains=self.request.GET.get('Model'),
                    service__service_centre__icontains=self.request.GET.get('Service'),
                    available__icontains=self.request.GET.get('Available'),
                    service__filial__slug=self.kwargs['slug']
                ).order_by(self.request.GET.get('sort', default='model__company__company'), 'model__model',
                           'service__service_centre')
        else:
            qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                   'model__add_filter_name', 'model__add_filter').filter(
                model__type_fk__slug=self.kwargs['cat_slug'], service__filial__slug=self.kwargs['slug'],
                model__actual='Да').order_by(
                self.request.GET.get('sort', default='model__company__company'), 'model__model',
                'service__service_centre')
        if Type.objects.select_related().filter(purpose__purpose='Абонентское', slug=self.kwargs['cat_slug']):
            return qs1
        else:
            return qs1.filter(available='+')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testertime"] = TesterTime.objects.select_related('service').filter(
            service__filial__slug=self.kwargs['slug']
        ).order_by('service')
        context["available"] = Available.objects.select_related(
            'model', 'service').filter(service__filial__slug=self.kwargs['slug'], model__actual="Да").order_by(
            'service__id')
        context["available_f"] = Available.objects.select_related('model', 'service').filter(
            model__type_fk__slug=self.kwargs['cat_slug'],
            service__filial__slug=self.kwargs['slug']).order_by(
            'service__id')
        context['typed'] = Models.objects.select_related('type_fk').filter(actual='Да').order_by('type_fk_id')
        context['typed1'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      model__actual='Да').order_by(
            'model__type_fk')
        context['test'] = Models.objects.select_related('type_fk', 'add_filter_name', 'company').filter(
            type_fk__slug=self.kwargs['cat_slug'], available__service__filial__slug=self.kwargs['slug'],
            actual='Да', available__available='+').order_by(
            'company__company')
        context['title'] = Type.objects.select_related().filter(slug__exact=self.kwargs['cat_slug'])[0]
        context['service'] = Service.objects.all()
        context['quantity'] = self.request.GET.get('quantity', default=8)
        context['sort'] = self.request.GET.get('sort', default='model__company__company')
        context['filial'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      quantity__gt=0, model__actual='Да').order_by(
            'model__type_fk_id', 'model__id')
        context['city'] = Filial.objects.select_related().filter(slug__exact=self.kwargs['slug'])[0]
        context['main_button'] = '/' + Filial.objects.select_related().filter(
            filial__exact=context['city']).values_list('slug', flat=True)[0] + '/'
        context['city17'] = Filial.objects.select_related().filter(
            filial__exact=context['city']).values_list('slug', flat=True)[0]
        return context


class SearchResults(ListView):
    model = Available
    template_name = 'main/searchresults.html'
    context_object_name = 'models'

    def get_queryset(self):
        sort = self.request.GET.get('sort', default='model__company__company')
        qs = Available.objects.select_related().filter(Q(model__actual="Да") &
                                                       Q(service__filial__slug=self.kwargs['slug']) &
                                                       Q(model__model__contains=self.request.GET.get('Search')) &
                                                       Q(available='+')).order_by(sort, 'model__model', 'service__service_centre')

        qs2 = Available.objects.select_related().filter(Q(model__actual="Да") &
                                                       Q(service__filial__slug=self.kwargs['slug']) &
                                                       Q(model__model__contains=self.request.GET.get('Search')) &
                                                       Q(model__type_fk__purpose__purpose='Абонентское')).order_by(sort, 'model__model', 'service__service_centre')

        qs3 = qs | qs2
        company = self.request.GET.get('Company')
        type_filter = self.request.GET.get('Type')

        if company or type_filter:
            return qs3.filter(Q(model__company__company__icontains=self.request.GET.get('Company')) &
                             Q(model__type_fk__type__icontains=type_filter)).order_by(sort, 'model__model',
                                                                                      'service__service_centre')
        return qs3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available"] = Available.objects.select_related(
            'model', 'service').filter(service__filial__slug=self.kwargs['slug'], model__actual="Да").order_by(
            'service__id')
        context['city'] = Filial.objects.select_related().filter(slug__exact=self.kwargs['slug'])[0]
        context['city17'] = Filial.objects.select_related().filter(
            filial__exact=context['city']).values_list('slug', flat=True)[0]
        context["available_f"] = Available.objects.select_related('model', 'service').filter(
            model__model__contains=self.request.GET.get('Search'),
            service__filial__slug=self.kwargs['slug']).order_by(
            'service__id')
        context["testertime"] = TesterTime.objects.select_related('service').filter(
            service__filial__slug=self.kwargs['slug']
        ).order_by('service')
        context['filial'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      quantity__gt=0, model__actual='Да').order_by(
            'model__type_fk_id', 'model__id')
        context['typed1'] = Available.objects.select_related().filter(service__filial__slug=self.kwargs['slug'],
                                                                      model__actual='Да').order_by(
            'model__type_fk')
        context['quantity'] = self.request.GET.get('quantity', default=8)
        context['sort'] = self.request.GET.get('sort', default='model__company__company')
        context['search'] = self.request.GET.get('Search')
        context['company'] = self.request.GET.get('Company')
        context['type_filter'] = self.request.GET.get('Type')
        context['customer_devices_filter'] = Models.objects.select_related().filter(
                model__contains=self.request.GET.get('Search'), available__service__filial__slug=self.kwargs['slug'],
                type_fk__purpose__purpose='Абонентское')
        if context['type_filter']:
            context['company_filter'] = Models.objects.select_related('type_fk', 'add_filter_name', 'company').filter(
                type_fk__type__icontains=context['type_filter'],
                model__contains=self.request.GET.get('Search'), available__service__filial__slug=self.kwargs['slug'],
                actual='Да', available__available='+').order_by(
                'company__company') | context['customer_devices_filter']
        else:
            context['company_filter'] = Models.objects.select_related('type_fk', 'add_filter_name', 'company').filter(
                model__contains=self.request.GET.get('Search'), available__service__filial__slug=self.kwargs['slug'],
                actual='Да', available__available='+').order_by(
                'company__company') | context['customer_devices_filter']

        context['type_filtered'] = Models.objects.select_related('type_fk', 'add_filter_name', 'company').filter(
            model__contains=self.request.GET.get('Search'), available__service__filial__slug=self.kwargs['slug'],
            actual='Да', available__available='+').order_by(
            'type_fk__type') | context['customer_devices_filter']
        return context



