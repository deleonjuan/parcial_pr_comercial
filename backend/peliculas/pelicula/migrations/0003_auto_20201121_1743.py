# Generated by Django 3.1.3 on 2020-11-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0002_auto_20201121_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.TextField(),
        ),
    ]
