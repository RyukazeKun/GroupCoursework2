from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Admin,Customer,Order,Device,Equipment)
class ViewAdmin(ImportExportModelAdmin):
    pass