from django.db import models

# Create your models here.
class SISWA(models.Model):
    NISN = models.CharField(max_length=50)
    NAMA = models.CharField(max_length=40)
    TTL = models.CharField(max_length=40)
    PHOTO = models.CharField(max_length=40)
    EMAIL = models.CharField(max_length=40)
    NILAI = models.CharField(max_length=40)
    ALAMAT = models.CharField(max_length=40)
    


    def __str__(self):
        return self.NISN

class mahasiswa(models.Model):
    NIM = models.CharField(max_length=50)
    NAMA = models.CharField(max_length=40)
    TTL = models.CharField(max_length=40)
    PHOTO = models.CharField(max_length=40)
    EMAIL = models.CharField(max_length=40)
    NILAI = models.CharField(max_length=40)
    ALAMAT = models.CharField(max_length=40)


    def __str__(self):
        return self.NIP