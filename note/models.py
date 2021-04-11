from django.db import models

#from ckeditor_uploader.fields import RichTextField
#from tinymce.models import HTMLField
#from ckeditor.fields import RichTextField
# from markitup.widgets import MarkItUpWidget
#from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
#from note import forms


class Note(models.Model):
    #title = RichTextField()
    title = models.TextField('Заметка')

    # content = HTMLField()
    # task = models.CharField('write', max_length=50)
    # date = models.DateTimeField('Дата')
    # time = models.TimeField('Время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
