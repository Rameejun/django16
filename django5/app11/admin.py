from django.contrib import admin
from app11.models import *
class employeeAdmin(admin.ModelAdmin):
    list_display = ["eid","name","age"]
# Register your models here.
admin.site.register(employee,employeeAdmin)
