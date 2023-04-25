from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name','username','date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields=('last_login', 'date_joined')
    ordering=('-date_joined',)
    filter_horizontal = []  # remove the filter_horizontal attributes that refer to groups and user_permissions
    list_filter = ()
    fieldsets = ()
   
    
    # remove the list_filter attributes that refer to is_superuser and groups
    # or modify them to refer to valid filter fields
    

# admin.site.register(Account, AccountAdmin)

    
admin.site.register(Account, AccountAdmin)