from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + " " + self.categoria
    
class Socio(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechaNac=models.DateField()
    dni=models.IntegerField()
    tel=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.nombre +" "+ self.apellido+" "+self.dni
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.IntegerField()
    disciplina=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.disciplina
    
    

