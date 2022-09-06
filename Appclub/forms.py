from django import forms


class FormSocio(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fechaNac_aaaa_mm_dd=forms.DateField()
    dni=forms.IntegerField()
    tel=forms.IntegerField()
    email=forms.EmailField()
    
class FormDisciplina(forms.Form):
    nombre=forms.CharField(max_length=50)
    categoria=forms.CharField(max_length=50)
    
class FormProfesor(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    tel=forms.IntegerField()
    disciplina=forms.CharField(max_length=50)