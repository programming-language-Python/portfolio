# Generated by Django 4.0.5 on 2022-06-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, upload_to='preview/', verbose_name='Фото'),
        ),
    ]
