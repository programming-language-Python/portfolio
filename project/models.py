from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")

    def __str__(self):
        return self.title

    photo = models.ImageField(
        upload_to='preview/', verbose_name='Превью', blank=True)
    programming_language = models.ForeignKey('ProgrammingLanguage', on_delete=models.PROTECT,
                                             verbose_name='Язык программирования')
    link = models.URLField(verbose_name="Ссылка")
    github = models.URLField(verbose_name="GitHub")
    description = models.TextField(verbose_name="Описание")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def some_field_html(self):
        return mark_safe(self.description)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['title']


class ProgrammingLanguage(models.Model):
    title = models.CharField(
        max_length=100, db_index=True, verbose_name='Язык программирования')

    def get_absolute_url(self):
        return reverse('programming_language', kwargs={"programming_language_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
        ordering = ['title']
