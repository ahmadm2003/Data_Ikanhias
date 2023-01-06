from django.forms import ModelForm
from django import forms
from ikanhias_app.models import ikan_hias

class Formikan_hias(ModelForm):
    class Meta:
        model = ikan_hias
        fields = '__all__'

        widgets ={
            'Nama ikan' : forms.TextInput({ 'class' : 'form-control'}),
            'Asal ikan' : forms.TextInput({ 'class' : 'form-control'}),
            'Harga' : forms.TextInput({ 'class' : 'form-control'}),
            'Gambar' : forms.TextInput({ 'class' : 'form-control'}),
            'Jenis id' : forms.TextInput({ 'class' : 'form-control'}),
            'Penjelasan' : forms.TextInput({ 'class' : 'form-control'}),
        }
