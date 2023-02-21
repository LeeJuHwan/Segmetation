from django.contrib import admin
from .models import FileUpload, DrugInfo

class FileAdmin(admin.ModelAdmin) :
    readonly_fields = ("id", )

class DbAdmin(admin.ModelAdmin) :
    id_field = ("id", )

# Register your models here.
admin.site.register(FileUpload, FileAdmin)
admin.site.register(DrugInfo, DbAdmin)
