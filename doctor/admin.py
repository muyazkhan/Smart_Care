from django.contrib import admin
from .models import specialization,designation,AvailableTime,Doctor,review
# Register your models here.
class specializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
admin.site.register(specialization,specializationAdmin)

class designationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
admin.site.register(designation,designationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(review)