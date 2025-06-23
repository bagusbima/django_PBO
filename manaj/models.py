from django.utils.translation import gettext_lazy as _
from django.db import models

class Kendaraan(models.Model):
    # Pilihan jenis kendaraan
    class JenisKendaraan(models.TextChoices):
        MOBIL = 'mobil', _('Mobil')
        MOTOR = 'motor', _('Motor')

    # Pilihan status kendaraan di garasi
    class StatusGarasi(models.TextChoices):
        TERPARKIR = 'terparkir', _('Terparkir')
        KELUAR = 'keluar', _('Keluar')
        PERAWATAN = 'perawatan', _('Dalam Perawatan')

    # Kolom-kolom informasi kendaraan
    nomor_polisi = models.CharField(max_length=15, unique=True)
    merek = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    jenis = models.CharField(
        max_length=10,
        choices=JenisKendaraan.choices,
        default=JenisKendaraan.MOBIL
    )
    status = models.CharField(
        max_length=15,
        choices=StatusGarasi.choices,
        default=StatusGarasi.TERPARKIR
    )
    waktu_masuk = models.DateTimeField(auto_now_add=True)
    waktu_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'garasi_kendaraan'

    def _str_(self):
        return f"{self.nomor_polisi} - {self.merek} {self.model}"
