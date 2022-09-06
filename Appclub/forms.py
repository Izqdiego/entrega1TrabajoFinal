from django import forms


class FormSocio(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fechaNac=forms.DateField()
    dni=forms.IntegerField()
    tel=forms.IntegerField()
    email=forms.EmailField()