from django.urls import path
from . import views
app_name = 'manaj'
urlpatterns = [
    path('', views.list_kendaraan, name='list_kendaraan'),
    path('tambah/', views.tambah_kendaraan, name='tambah_kendaraan'),
    path('edit/<int:id>/', views.kendaraan_edit, name='kendaraan_edit'),
    path('delete/<int:id>/', views.kendaraan_delete, name='kendaraan_delete'),
]
