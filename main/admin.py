

from django.contrib import admin
from .models import (AllowedCombination, Service, Category_abon, Good, Order, OrderItem,
                     Subcategory, State, Router, Zala, SmartHome, Tv, Notebook, Pad, Watch,
                     Scooter, Vacuum, Coffee, Conditioner, Other, Purpose, Available, Models, SmartSpeaker)

admin.site.register(Service)
admin.site.register(Category_abon)
admin.site.register(Subcategory)
admin.site.register(Good)
admin.site.register(State)
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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem, OrderItemAdmin)


class AllowedCombinationAdmin(admin.ModelAdmin):
    list_display = ['cat', 'subcat', 'good', ]


admin.site.register(AllowedCombination, AllowedCombinationAdmin)


class AvailableAdmin(admin.ModelAdmin):
    list_display = ['service', 'model', 'available', 'quantity']
    list_filter = ['service', 'model', 'available']


admin.site.register(Available, AvailableAdmin)
