
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
admin.site.index_title = "Добро пожаловать"
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
    save_as = True
    def Тип(self, obj):
        return obj.model.type

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
        else:
            return self.model.objects.all()




    def get_form(self, request, obj=None, **kwargs):
        form = super(AvailableAdmin, self).get_form(request, obj, **kwargs)
        latest_object = Available.objects.latest('date')
        form.base_fields['model'].initial = latest_object.model
        form.base_fields['company'].initial = latest_object.company
        form.base_fields['quantity'].initial = latest_object.quantity
        form.base_fields['available'].initial = latest_object.available

        return form

    list_display = ['service', 'Тип', 'company', 'model', 'date', 'available', 'quantity']
    list_filter = ['model__type', 'company', 'available']
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