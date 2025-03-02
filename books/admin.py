from django.contrib import admin
from .models import Books

class AdminBooks(admin.ModelAdmin):
    list_display=['title', 'author']

# Register your models here.
admin.site.register(Books,AdminBooks)