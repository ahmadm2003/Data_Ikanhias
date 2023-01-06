from django.contrib import admin

# Register your models here.
from .models import *

class ikanhias_admin(admin.ModelAdmin):
    list_display = ['nama_ikan', 'asal_ikan', 'harga', 'gambar']
    search_fields = ['nama_ikan', 'asal_ikan', 'harga']
    list_filter = ['jenis_id']
    list_per_page = 4

admin.site.register(ikan_hias, ikanhias_admin)
admin.site.register(jenis)
