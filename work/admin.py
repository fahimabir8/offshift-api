from django.contrib import admin
from .models import Category,Work,Proposal

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    list_display = ['name','slug',]
    
class CustomWork(admin.ModelAdmin):
    list_display = ['title','client','freelancer',]

class CustomProposal(admin.ModelAdmin):
    list_display = ['work','client','freelancer',]
admin.site.register(Category,CategoryAdmin)
admin.site.register(Work,CustomWork)
admin.site.register(Proposal,CustomProposal)