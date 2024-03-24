from django.contrib import admin
from .models import Task, SubTask, Category, Contact

class TaskAdmin(admin.ModelAdmin):
    # Dies ermöglicht eine einfachere Auswahl und Zuweisung von Kontakten zu einem Task
    filter_horizontal = ('assigned_to',)
    # oder filter_vertical = ('assigned_to',) je nach Vorliebe

admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask)
admin.site.register(Category)
admin.site.register(Contact)