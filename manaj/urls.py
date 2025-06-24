from django.urls import path
from . import views
app_name = 'manaj'
urlpatterns = [
    path('', views.list_kendaraan, name='list_kendaraan'),
    path('tambah/', views.tambah_kendaraan, name='tambah_kendaraan'),
    path('edit/<int:id>/', views.kendaraan_edit, name='kendaraan_edit'),
    path('delete/<int:id>/', views.kendaraan_delete, name='kendaraan_delete'),
    path('pajak/', views.list_pajak, name='list_pajak'),
    path('pajak/tambah/', views.tambah_pajak, name='tambah_pajak'),
    path('pajak/edit/<int:id>/', views.edit_pajak, name='edit_pajak'),
    path('pajak/delete/<int:id>/', views.delete_pajak, name='delete_pajak'),

]
