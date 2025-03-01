from django.contrib import admin
from . models import date
from . models import mgt
from . models import vendor,User,Register

admin.site.register(User)
#admin.site.register(mgt)
admin.site.register(date)
#admin.site.register(vendor)
admin.site.register(Register)

@admin.register(vendor)
class vendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'v_total','id')
    ordering = ('name',)
    search_fields = ('name', 'v_total')

@admin.register(mgt)
class mgtAdmin(admin.ModelAdmin):
    list_display = ('date', 'vendor','vegetable_name','total' )
   
   


