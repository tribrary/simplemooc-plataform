# Generated by Django 3.1.2 on 2020-12-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201217_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/images', verbose_name='Imagem'),
        ),
    ]
