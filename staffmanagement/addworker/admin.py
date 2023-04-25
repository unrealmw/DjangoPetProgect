from django.contrib import admin

# Register your models here.
from .models import Worker, Department


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'patronymic', 'birth_date', 'department')
    list_display_links = ('name', 'last_name')
    search_fields = ("name", "last_name")


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Department, DepartmentAdmin)
