# Generated by Django 4.0.5 on 2022-06-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>/', verbose_name='Фото'),
        ),
    ]
