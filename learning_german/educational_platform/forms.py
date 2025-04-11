from django import forms
from .models import Word

class AddWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['german_word', 'russian_translation', 'difficulty']
        widgets = {
            'german_word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите слово на немецком'
            }),
            'russian_translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите перевод на русский'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select'
            })
        }
        labels = {
            'german_word': 'Немецкое слово',
            'russian_translation': 'Русский перевод',
            'difficulty': 'Уровень сложности'
        }

    def clean_german_word(self):
        german_word = self.cleaned_data['german_word']
        if not all(char.isalpha() or char.isspace() or char in '-ßäöüÄÖÜ' for char in german_word):
            raise forms.ValidationError("Немецкое слово содержит недопустимые символы")
        return german_word

    def clean_russian_translation(self):
        russian_translation = self.cleaned_data['russian_translation']
        if not all(char.isalpha() or char.isspace() or char in '-' for char in russian_translation):
            raise forms.ValidationError("Русский перевод содержит недопустимые символы")
        return russian_translation