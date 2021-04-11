from django.shortcuts import render#, redirect
from .models import Note
from .forms import NoteForm
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse


def index(request):
    error = ' '
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('home')
        else:
            error = 'Форма не корректна'
    form = NoteForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'note/index.html', context)


def note(request):
    notes = Note.objects.all()
    return render(request, 'note/index.html', {'title': 'Главная страничка', 'title': notes})


