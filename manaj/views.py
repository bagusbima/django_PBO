from django.shortcuts import render, redirect, get_object_or_404
from .models import Kendaraan
from .forms import KendaraanForm
from django.http import Http404
from django.contrib import messages
from .models import Pajak
from .forms import PajakForm
from datetime import datetime
from django.db.models import Q

def list_kendaraan(request):
    query = request.GET.get('q', '')
    kendaraan_list = Kendaraan.objects.all()

    if query:
        kendaraan_list = kendaraan_list.filter(
            Q(nomor_polisi__icontains=query) |
            Q(merek__icontains=query) |
            Q(model__icontains=query) |
            Q(jenis__icontains=query) |
            Q(status__icontains=query)
        )

    return render(request, 'manaj/list_kendaraan.html', {
        'kendaraan_list': kendaraan_list,
        'query': query,
    })


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
            return redirect('manaj:list_kendaraan')
    else:
        form = KendaraanForm(instance=kendaraan)
    return render(request, 'manaj/form_kendaraan.html', {'form': form, 'edit': True})

def kendaraan_delete(request, id):
    kendaraan = get_object_or_404(Kendaraan, id=id)
    if request.method == 'POST':
        kendaraan.delete()
        messages.success(request, 'Kendaraan berhasil dihapus.')
        return redirect('manaj:list_kendaraan')
    return render(request, 'manaj/confirm_delete.html', {'kendaraan': kendaraan})

def tambah_kendaraan(request):
    form = KendaraanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kendaraan berhasil ditambahkan.')
        return redirect('manaj:list_kendaraan')
    return render(request, 'manaj/form_kendaraan.html', {
        'form': form,
        'title': 'Tambah Kendaraan',
        'edit': False
    })

def list_pajak(request):
    urutan = request.GET.get('urut', 'asc')

    if urutan == 'desc':
        pajak_list = Pajak.objects.all().order_by('-tanggal_jatuh_tempo')
    else:
        pajak_list = Pajak.objects.all().order_by('tanggal_jatuh_tempo')


    return render(request, 'manaj/list_pajak.html', {
        'pajak_list': pajak_list,
        'urutan': urutan
    })


def tambah_pajak(request):
    form = PajakForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('manaj:list_pajak')
    return render(request, 'manaj/form_pajak.html', {'form': form, 'title': 'Tambah Pajak'})
def edit_pajak(request, id):
    pajak = get_object_or_404(Pajak, id=id)
    form = PajakForm(request.POST or None, instance=pajak)
    if form.is_valid():
        form.save()
        return redirect('manaj:list_pajak')
    return render(request, 'manaj/form_pajak.html', {'form': form, 'edit': True, 'title': 'Edit Pajak'})

def delete_pajak(request, id):
    pajak = get_object_or_404(Pajak, id=id)
    if request.method == 'POST':
        pajak.delete()
        messages.success(request, "Pajak berhasil dihapus.")
        return redirect('manaj:list_pajak')
    return render(request, 'manaj/confirm_delete_pajak.html', {'pajak': pajak})



from django.shortcuts import render

# Create your views here.
