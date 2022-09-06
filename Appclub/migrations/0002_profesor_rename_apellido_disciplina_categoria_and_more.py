# Generated by Django 4.1 on 2022-09-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appclub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('disciplina', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='apellido',
            new_name='categoria',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='email',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='tel',
        ),
    ]