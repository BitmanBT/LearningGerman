from django.shortcuts import render
from .models import Word


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
    return render(request, 'educational_platform/add_words.html')