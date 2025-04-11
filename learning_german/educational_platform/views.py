from django.shortcuts import render, redirect
from django.contrib import messages
from random import sample, shuffle
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
    all_words = list(Word.objects.all())
    
    if not all_words:
        return render(request, 'educational_platform/exercises.html', {'no_words': True})
    
    context = {}
    
    if request.method == 'POST' and 'selected_option_id' in request.POST:
        selected_id = int(request.POST['selected_option_id'])
        correct_id = int(request.POST['correct_word_id'])
        correct_word = Word.objects.get(id=correct_id)
        
        context.update({
            'direction': request.POST['direction'],
            'word_to_translate': request.POST['word_to_translate'],
            'options': [
                {
                    'id': int(id),
                    'text': text,
                    'is_correct': int(id) == correct_id
                }
                for id, text in zip(
                    request.POST.getlist('option_ids'),
                    request.POST.getlist('option_texts')
                )
            ],
            'feedback': {
                'is_correct': selected_id == correct_id,
                'correct_answer': correct_word.russian_translation if request.POST['direction'] == 'de-ru' else correct_word.german_word,
                'selected_id': selected_id
            },
            'show_result': True
        })
    else:
        correct_word = sample(all_words, 1)[0]
        other_words = [w for w in all_words if w.id != correct_word.id]
        wrong_options = sample(other_words, min(3, len(other_words)))
        options = [correct_word] + wrong_options
        shuffle(options)
        
        direction = 'de-ru' if sample([True, False], 1)[0] else 'ru-de'
        
        context.update({
            'direction': direction,
            'word_to_translate': correct_word.german_word if direction == 'de-ru' else correct_word.russian_translation,
            'options': [
                {
                    'id': word.id,
                    'text': word.russian_translation if direction == 'de-ru' else word.german_word,
                    'is_correct': word.id == correct_word.id
                }
                for word in options
            ],
            'correct_word_id': correct_word.id,
            'show_result': False
        })
    return render(request, 'educational_platform/exercises.html', context)

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