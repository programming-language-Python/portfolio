from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project, ProgrammingLanguage


# Register your models here.
class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = (
        'id', 'get_photo', 'title', 'programming_language', 'link', 'github', 'some_field_html', 'date_added')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'programming_language', 'some_field_html', 'date_added')
    list_editable = ('programming_language',)
    list_filter = ('id', 'title', 'programming_language', 'description', 'date_added')
    fields = ('photo', 'title', 'programming_language', 'link', 'github', 'description', 'date_added')
    readonly_fields = ('date_added',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Превью'


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)

admin.site.site_title = 'Управление проектами'
admin.site.site_header = 'Управление проектами'
