from django.shortcuts import render, redirect, get_object_or_404
from .models import Kendaraan
from .forms import KendaraanForm

def list_kendaraan(request):
    kendaraan_list = Kendaraan.objects.all()
    context = {
        'kendaraan_list': kendaraan_list
    }
    return render(request, 'manaj/list_kendaraan.html', context)


def tambah_kendaraan(request):
    form = KendaraanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_kendaraan')
    return render(request, 'kendaraan_form.html', {'form': form, 'title': 'Tambah Kendaraan'})

def kendaraan_edit(request, id):
    kendaraan = get_object_or_404(Kendaraan, id=id)
    if request.method == 'POST':
        form = KendaraanForm(request.POST, instance=kendaraan)
        if form.is_valid():
            form.save()
            return redirect('kendaraan_list')
    else:
        form = KendaraanForm(instance=kendaraan)
    return render(request, 'manaj/form_kendaraan.html', {'form': form, 'edit': True})

def kendaraan_delete(request, id):
    kendaraan = get_object_or_404(Kendaraan, id=id)
    if request.method == 'POST':
        kendaraan.delete()
        return redirect('kendaraan_list')
    return render(request, 'manaj/confirm_delete.html', {'kendaraan': kendaraan})
