from django.contrib import admin
from tasks.models import Task

class Tasks(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Task, Tasks)
# Register your models here.
