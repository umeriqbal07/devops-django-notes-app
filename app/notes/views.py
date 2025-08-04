from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Note

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('index')


def index(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'add_note.html')
