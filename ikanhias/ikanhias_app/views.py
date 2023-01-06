from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.models import User
from ikanhias_app.models import ikan_hias
from ikanhias_app.forms import Formikan_hias
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def ubahikanhias(request, id_fish):
    fish = ikan_hias.objects.get(id=id_fish)
    template = 'ubahikanhias.html'
    if request.POST:
        form = Formikan_hias(request.POST, instance=fish)
        if form.is_valid():
            form.save()
            return redirect('ubahikanhias', id_fish=id_fish)
    else:
        form = Formikan_hias(instance=fish)
        konteks = {
            'form':form,
            'fish':fish,
        }
    return render (request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def halamandata(request):
    fish = ikan_hias.objects.all()
    data = {
        'Title' : "Halaman Data Ikan Hias",
        'Heading' : "Data Ikan Hias",
        'fish' : fish,
    }
    return render(request, "halamandata.html", data)

@login_required(login_url=settings.LOGIN_URL)
def halamanasal(request):
    fish = ikan_hias.objects.all()
    data = {
        'Title' : "Halaman Asal Ikan Hias",
        'Heading' : "Data Asal Ikan Hias",
        'fish' : fish,
    }
    return render(request, "halamanasal.html", data)

@login_required(login_url=settings.LOGIN_URL)
def halamanharga(request):
    fish = ikan_hias.objects.all()
    data = {
        'Title' : "Halaman Harga Ikan Hias",
        'Heading' : "Data Harga Ikan Hias",
        'fish' : fish,
    }
    return render(request, "halamanharga.html", data)

@login_required(login_url=settings.LOGIN_URL)
def halamanaksi(request, id):
    fish = ikan_hias.objects.get(pk=id)
    data = {
        'Title' : "Halaman Detail Ikan Hias",
        'Heading' : "Data Detail Ikan Hias",
        'fish' : fish,
    }
    return render(request, "halamanaksi.html", data)

@login_required(login_url=settings.LOGIN_URL)
def tambahikan_hias(request):
    if request.POST:
        form = Formikan_hias(request.POST)
        if form.is_valid():
            form.save()
            form = Formikan_hias()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form':form,
                'pesan':pesan,
             }

            return render(request, 'tambahikanhias.html', konteks)
    
    else:
        form = Formikan_hias()

        konteks = {
        'form':form,
    }

    return render(request, 'tambahikanhias.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def deleteikan_hias(request, id_ikan_hias):
    ikan_hias = ikan_hias.objects.get(id=id_ikan_hias)
    ikan_hias.delete()

    return redirect('/halamandata/') 
