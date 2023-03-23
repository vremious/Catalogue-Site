
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'action_time', 'user', 'content_type', 'object_repr')
    list_filter = ('content_type','user__username')
    search_fields = ['user__username']
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

admin.site.register(Company)
admin.site.register(Router)
admin.site.register(Zala)
admin.site.register(SmartHome)
admin.site.register(Tv)
admin.site.register(Notebook)
admin.site.register(Pad)
admin.site.register(Watch)
admin.site.register(Scooter)
admin.site.register(Vacuum)
admin.site.register(Coffee)
admin.site.register(Conditioner)
admin.site.register(Other)
admin.site.register(Purpose)
admin.site.register(SmartSpeaker)
admin.site.register(Models)
admin.site.register(Smartphone)
admin.site.register(Service)
admin.site.register(Speaker)

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
#

class AvailableAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_max_show_all = 1000
    save_as = True


    @admin.display(ordering='model__type', description='Тип')
    def type(self, obj):
        return obj.model.type
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

    list_display = ['service', 'type', 'company', 'model', 'date', 'available', 'quantity']
    list_filter = ['model__type', 'model__company', 'available']
    list_editable = ['available', 'quantity']
    search_fields = ['model__model']



admin.site.register(Available, AvailableAdmin)



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

# messages.add_message(request, messages.INFO, "Hello world.")
def logged_in_message(sender, user, request, **kwargs):
    """
    Add a welcome message when the user logs in
    """
    messages.info(request, "Обновления от 23.03:"
                  )
    messages.info(request, "1) Добавлено недостающее оборудование в каталог, устранены мелкие неточности, удалены дубли некоторого оборудования"
                  )
    messages.info(request, "2) В администрировании в фильтрах теперь есть 'Кофеварки' и 'Кофемашины'"
                  )
    messages.info(request,   "Если есть предложения/вопросы/пожелания, их можно отправить на Emelyanov_da@mgts.by, также есть рабочий номер телефона 290-57-12"
                  )

user_logged_in.connect(logged_in_message)