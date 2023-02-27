from django.forms import ModelForm, FileField, FileInput
from .models import FileUpload
from django import forms

class UploadForm(ModelForm): 
    class Meta:
        model = FileUpload
        fields = "__all__"
