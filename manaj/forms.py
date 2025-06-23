# manaj/forms.py
from django import forms
from .models import Kendaraan

class KendaraanForm(forms.ModelForm):
    class Meta:
        model = Kendaraan
        fields = '__all__'
