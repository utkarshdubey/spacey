from django.contrib import admin
from .models import Planet
from import_export.admin import ImportExportModelAdmin

@admin.register(Planet)
class PersonAdmin(ImportExportModelAdmin):
	pass