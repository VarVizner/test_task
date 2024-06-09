from django.contrib import admin
from .models import Elements

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


admin.site.register(Elements)


class Products(ImportExportActionModelAdmin):
    resource_class = Elements
