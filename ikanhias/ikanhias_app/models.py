from django.db import models

# Create your models here.

class jenis(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class ikan_hias(models.Model):
    nama_ikan = models.CharField(max_length=50)
    asal_ikan = models.CharField(max_length=40)
    harga = models.IntegerField(null=True)
    gambar = models.CharField(max_length=70, null=True)
    jenis_id = models.ForeignKey(jenis, on_delete=models.CASCADE, null=True)
    penjelasan = models.TextField(null=True)

    def __str__(self):
        return self.nama_ikan