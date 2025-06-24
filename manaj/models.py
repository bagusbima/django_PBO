from django.utils.translation import gettext_lazy as _
from django.db import models

class Kendaraan(models.Model):
    class JenisKendaraan(models.TextChoices):
        MOBIL = 'mobil', _('Mobil')
        MOTOR = 'motor', _('Motor')

    class StatusGarasi(models.TextChoices):
        TERPARKIR = 'terparkir', _('Terparkir')
        KELUAR = 'keluar', _('Keluar')
        PERAWATAN = 'perawatan', _('Dalam Perawatan')

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
    
class Pajak(models.Model):
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE, related_name='pajaks')
    tanggal_jatuh_tempo = models.DateField()
    nominal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'garasi_pajak'

    def __str__(self):
        return f"Pajak {self.kendaraan.nomor_polisi} - {self.kendaraan.merek}"
