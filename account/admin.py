from django.contrib import admin
from .models import CustomUser,Review
from django.contrib.auth.admin import UserAdmin

class Customs(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'user_type',]
    fields = ['username','first_name','last_name','email','user_type','country','about_me','image']
admin.site.register(CustomUser,Customs)
admin.site.register(Review)

