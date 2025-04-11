from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Word
from .forms import AddWordForm


def index(request):
    return render(request, 'educational_platform/index.html')

def vocabulary(request):
    words = Word.objects.all().order_by('german_word')
    
    difficulty_filter = request.GET.get('difficulty')
    if difficulty_filter:
        words = words.filter(difficulty=difficulty_filter)
    
    context = {
        'words': words,
        'difficulty_choices': Word.DIFFICULTY_CHOICES,
        'current_difficulty': difficulty_filter,
    }
    return render(request, 'educational_platform/vocabulary.html', context)

def exercises(request):
    return render(request, 'educational_platform/exercises.html')

def add_words(request):
    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Слово успешно добавлено в словарь!')
            return redirect('add_words')
    else:
        form = AddWordForm()
    return render(request, 'educational_platform/add_words.html', {'form': form})