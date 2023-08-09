from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Sum

from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'action_time' ,'user', 'object_repr')
    list_filter = ('user__username',)
    search_fields = ['object_repr']
    date_hierarchy = 'action_time'

admin.site.register(LogEntry, LogEntryAdmin)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

User = get_user_model()
admin.site.site_header = "Администрирование оборудования Белтелеком"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать!"
admin.site.register(Type)
admin.site.register(Company)
admin.site.register(Other)
admin.site.register(Purpose)
admin.site.register(Service)
admin.site.register(Speaker)
admin.site.register(Console)
admin.site.register(Cooking)


class ModelsAdmin(admin.ModelAdmin):


    list_display = ['company', 'model', 'type_fk']
    list_filter = ['company']
    search_fields = ['model']
    list_editable = ['type_fk']

admin.site.register(Models, ModelsAdmin)

class RouterAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model


    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Router,RouterAdmin)

class ZalaAdmin(admin.ModelAdmin):
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Zala,ZalaAdmin)


class SmartHomeAdmin(admin.ModelAdmin):
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(SmartHome, SmartHomeAdmin)

class TVAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model','size']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Tv, TVAdmin)


class NotebookAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Notebook, NotebookAdmin)

class PadAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Pad, PadAdmin)

class WatchAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Watch, WatchAdmin)

class ScooterAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Scooter, ScooterAdmin)

class VacuumAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Vacuum, VacuumAdmin)


class ConditionerAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Conditioner, ConditionerAdmin)

class CoffeeAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Coffee, CoffeeAdmin)


class SmartphoneAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Smartphone, SmartphoneAdmin)

class SmartSpeakerAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(SmartSpeaker, SmartSpeakerAdmin)


class BikesAdmin(admin.ModelAdmin):
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    list_display = ['company', 'model']
    list_filter = ['model__company']
    search_fields = ['model__model']

admin.site.register(Bikes, BikesAdmin)

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 0
#
#
# class OrderAdmin(admin.ModelAdmin):
#     inlines = [OrderItemInline]
#
#
# admin.site.register(Order, OrderAdmin)
#
#
# class OrderItemAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(OrderItem, OrderItemAdmin)
#
#
# class AllowedCombinationAdmin(admin.ModelAdmin):
#     list_display = ['cat', 'subcat', 'good', ]
#
#
# admin.site.register(AllowedCombination, AllowedCombinationAdmin)


@admin.register(Available)
class AvailableAdmin(ModelAdminTotals):
    list_per_page = 20
    list_max_show_all = 5000
    save_as = True


    @admin.display(ordering='model__type', description='Тип')
    def type(self, obj):
        return obj.model.type_fk
    @admin.display(ordering='model__company', description='Производитель')
    def company(self, obj):
        return obj.model.company
    @admin.display(ordering='model__model', description='Модель')
    def model(self, obj):
        return obj.model.model

    class Media:
        js = ['js/admin_filter.js']


    def get_queryset(self, request):
        if request.user.username == 'UPU1':
            return self.model.objects.filter(
                service='1'
            )
        if request.user.username == 'UPU2':
            return self.model.objects.filter(
                service='2'
            )
        if request.user.username == 'UPU3':
            return self.model.objects.filter(
                service='3'
            )
        if request.user.username == 'UPU4':
            return self.model.objects.filter(
                service='4'
            )
        if request.user.username == 'UPU5':
            return self.model.objects.filter(
                service='5'
            )
        if request.user.username == 'GSPP':
            return self.model.objects.filter(
                service='6'
            )
        else:
            return self.model.objects.all()




    def get_form(self, request, obj=None, **kwargs):
        form = super(AvailableAdmin, self).get_form(request, obj, **kwargs)
        latest_object = Available.objects.latest('date')
        form.base_fields['model'].initial = latest_object.model
        # form.base_fields['company'].initial = latest_object.company
        form.base_fields['quantity'].initial = latest_object.quantity
        form.base_fields['available'].initial = latest_object.available

        return form


    list_filter = ['model__type_fk', 'model__company', 'available', 'service']
    list_editable = ['available', 'quantity']
    list_display = ['service', 'type', 'company', 'model', 'date', 'available', 'quantity']
    list_totals = [('quantity', Sum)]
    search_fields = ['model__model']



# admin.site.register(Available, AvailableAdmin)






class TesterTimeAdmin(admin.ModelAdmin):
    save_as = True

    def get_queryset(self, request):
        if request.user.username == 'UPU1':
            return self.model.objects.filter(
                service='1'
            )
        if request.user.username == 'UPU2':
            return self.model.objects.filter(
                service='2'
            )
        if request.user.username == 'UPU3':
            return self.model.objects.filter(
                service='3'
            )
        if request.user.username == 'UPU4':
            return self.model.objects.filter(
                service='4'
            )
        if request.user.username == 'UPU5':
            return self.model.objects.filter(
                service='5'
            )
        if request.user.username == 'GSPP':
            return self.model.objects.filter(
                service='6'
            )
        else:
            return self.model.objects.all()




    def get_form(self, request, obj=None, **kwargs):
        form = super(TesterTimeAdmin, self).get_form(request, obj, **kwargs)
        latest_object = TesterTime.objects.latest('date')
        form.base_fields['worktime'].initial = latest_object.worktime

        return form

    list_display = ['service', 'worktime', 'onduty']
    list_editable = ['worktime', 'onduty']



admin.site.register(TesterTime, TesterTimeAdmin)

from django.contrib import messages
from django.contrib.auth.signals import user_logged_in

def logged_in_message(sender, user, request, **kwargs):
    """
    Add a welcome message when the user logs in
    """
    messages.info(request, "Добро пожаловать!"
                  )
    # messages.info(request, "Категория 'Роботы-пылесосы' переименована в 'Пылесосы', т.к. в будущем планируется добавление вертикальных пылесосов"
    #               )
    # messages.info(request, "В связи с этим прошу всех администарторов СЦ вводить актуальную информацию по наличию оборудования, а также проверить рванее введённые данные."
    #              )
    # messages.info(request, "Также есть предложение создать рабочий чат (Телеграмм или Вайбер) для оперативного решения вопросов связанных с работой портала"
    #              )
    # messages.info(request, "Свои номера отправляйте на почту Emelyanov_da@mgts.by"
    #              )

user_logged_in.connect(logged_in_message)