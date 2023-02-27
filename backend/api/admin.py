from django.contrib import admin
from .models import FileUpload, DrugInfo, User, DrugInfoEfcy, DrugMaterial

class UserAdmin(admin.ModelAdmin) :
    id_field = ("id", )

class FileAdmin(admin.ModelAdmin) :
    readonly_fields = ("id", )

class DbAdmin(admin.ModelAdmin) :
    id_field = ("id", )

class InfoAdmin(admin.ModelAdmin) :
    id_field = ("id", )

class MateAdmin(admin.ModelAdmin) :
    id_field = ("id", )
    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(FileUpload, FileAdmin)
admin.site.register(DrugInfo, DbAdmin)
admin.site.register(DrugInfoEfcy, InfoAdmin)
admin.site.register(DrugMaterial, MateAdmin)

