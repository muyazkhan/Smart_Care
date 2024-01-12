from django.contrib import admin
from .models import Contact_Us
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
  list_display=['name','phone','problem']
admin.site.register(Contact_Us,ContactModelAdmin)