# manaj/forms.py
from django import forms
from .models import Kendaraan
from .models import Pajak

class KendaraanForm(forms.ModelForm):
    class Meta:
        model = Kendaraan
        fields = '__all__'

class PajakForm(forms.ModelForm):
    class Meta:
        model = Pajak
        fields = ['kendaraan', 'tanggal_jatuh_tempo', 'nominal']