from django.contrib import admin
from .models import TestProject, TestEnv, TestFile

# Register your models here.

@admin.register(TestProject)
class TestProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'leader']

@admin.register(TestEnv)
class TestEnvAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project']

@admin.register(TestFile)
class TestFiletAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'info']