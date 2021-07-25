from django.contrib import admin
from .models import MasterUser

# Register your models here.

class MasterUserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','first_name','last_name','password','email','mobile']



admin.site.register(MasterUser,MasterUserAdmin)