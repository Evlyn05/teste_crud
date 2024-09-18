from django.forms import ModelForm
from django import forms
from .models import Carro

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'
      
        widgets = {
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'modelo': forms.TextInput(attrs={'class': 'form-control' }),
            'cor': forms.TextInput(attrs={'class': 'form-control' }),
            'ano': forms.NumberInput(attrs={'class': 'form-control' }),
            'marca': forms.Select(attrs={'class': 'form-control' }),
        }