from .models import Note
from django.forms import ModelForm, Textarea
#from markitup.widgets import MarkItUpWidget


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title"]
        widgets = {
            "title": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Пиши'
            })

        }


#class MyForm(forms.Form):
    #content = forms.CharField(widget=MarkItUpWidget())
