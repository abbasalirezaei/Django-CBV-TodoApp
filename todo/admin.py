from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'created_date','isCompleted')

admin.site.register(Task, TaskAdmin)
