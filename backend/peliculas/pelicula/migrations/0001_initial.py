# Generated by Django 3.1.3 on 2020-11-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('estreno', models.CharField(max_length=5)),
                ('genero', models.CharField(choices=[('romance', 'romance'), ('accion', 'accion'), ('comedia', 'comedia'), ('terror', 'terror'), ('sifi', 'sifi'), ('animacion', 'animacion'), ('musical', 'musical')], default='romance', max_length=10)),
            ],
        ),
    ]
