from django.shortcuts import render


def index(request):
    return render(request, 'educational_platform/index.html')

def vocabulary(request):
    return render(request, 'educational_platform/vocabulary.html')

def exercises(request):
    return render(request, 'educational_platform/exercises.html')

def add_words(request):
    return render(request, 'educational_platform/add_words.html')