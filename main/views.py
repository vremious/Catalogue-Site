from django.views.generic import ListView
from .models import *


class MainPage(ListView):
    model = Models
    template_name = "main/category_detail.html"
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["testertime"] = TesterTime.objects.all().select_related('service').order_by('service')
        context['typed'] = Models.objects.select_related('type_fk', 'type_fk__purpose').filter(actual='Да').order_by('type_fk_id')
        context['typed1'] = Models.objects.select_related('type_fk', 'type_fk__purpose').filter(actual='Да').order_by('type_fk__type')
        context['type'] = Type.objects.all().select_related('purpose')
        context['image'] = Models.objects.values_list('image', 'id').first()
        context['title'] = 'Главная страница'
        return context


class CategoryPage(ListView):
    model = Models
    template_name = "main/upu4.html"
    context_object_name = 'models'

    def get_queryset(self):
        if self.request.GET.get('Company') or self.request.GET.get('Model') or self.request.GET.get('Service') or self.\
                request.GET.get('Available') or self.request.GET.get('Add_filter'):
            if self.request.GET.get('Add_filter'):
                qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                       'model__add_filter', 'model__add_filter_name').filter(
                    model__type_fk__slug=self.kwargs['cat_slug'], model__actual='Да',
                    model__company__company__icontains=self.request.GET.get('Company'),
                    model__model__icontains=self.request.GET.get('Model'),
                    service__service_centre__icontains=self.request.GET.get('Service'),
                    available__icontains=self.request.GET.get('Available'),
                    model__add_filter__value__icontains=self.request.GET.get('Add_filter'),
                    ).order_by('model__company__company', 'model__model',
                               'model__add_filter__value')
            else:
                qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                       'model__add_filter_name', 'model__add_filter').filter(
                    model__type_fk__slug=self.kwargs['cat_slug'], model__actual='Да',
                    model__company__company__icontains=self.request.GET.get('Company'),
                    model__model__icontains=self.request.GET.get('Model'),
                    service__service_centre__icontains=self.request.GET.get('Service'),
                    available__icontains=self.request.GET.get('Available'),

                    ).order_by('model__company__company', 'model__model')
        else:
            qs1 = Available.objects.select_related('model', 'service', 'model__company',
                                                    'model__add_filter_name', 'model__add_filter').filter(
                model__type_fk__slug=self.kwargs['cat_slug'], model__actual='Да',
                ).order_by('model__company__company', 'model__model',
                           'service__service_centre')
        return qs1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testertime"] = TesterTime.objects.all().select_related('service').order_by('service')
        context["available"] = Available.objects.all().select_related('model', 'service').order_by('service__id')
        context["available_f"] = Available.objects.select_related('model', 'service').filter(
            model__type_fk__slug=self.kwargs['cat_slug']).order_by(
            'service__id')
        context['typed'] = Models.objects.select_related('type_fk').filter(actual='Да').order_by('type_fk_id')
        context['typed1'] = Models.objects.select_related('type_fk', 'type_fk__purpose').filter(actual='Да').order_by('type_fk__type')
        context['test'] = Models.objects.select_related('type_fk', 'add_filter_name', 'company').filter(
            type_fk__slug=self.kwargs['cat_slug'], actual='Да').order_by(
            'company__company')
        context['title'] = str(context['test'][0].type_fk)
        return context
