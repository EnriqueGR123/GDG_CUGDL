from django.contrib import admin
from .models import task
# Register your models here.

class taskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
admin.site.register(task, taskAdmin)