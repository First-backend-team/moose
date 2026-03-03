from django.contrib import admin
from .models import ContactUS
# Register your models here.

@admin.register(ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject')
    list_display_links = ('full_name', 'email')

# @admin.register(ContactInfo)
# class ContactInfoAdmin(admin.ModelAdmin):
#     list_display = ('address', 'phone')
#     list_display_links = ('address', 'phone')