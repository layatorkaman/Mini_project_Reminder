from django.contrib import admin
from .models import Task, CategoryTask


# Register your models here

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'expire_date')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Task, TaskAdmin)
admin.site.register(CategoryTask)
