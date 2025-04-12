"""This module is responsible for the forms that the application uses"""
from django import forms
from .models import Word

class AddWordForm(forms.ModelForm):
    """A class for a form for adding new words to the database"""
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
        """Checks the correctness of the entered word in German"""
        german_word = self.cleaned_data['german_word']
        if not all(char.isalpha() or char.isspace() or char in '-ßäöüÄÖÜ' for char in german_word):
            raise forms.ValidationError("Немецкое слово содержит недопустимые символы")
        return german_word

    def clean_russian_translation(self):
        """Checks the correctness of the entered translation in Russian"""
        russian_translation = self.cleaned_data['russian_translation']
        if not all(char.isalpha() or char.isspace() or char in '-' for char in russian_translation):
            raise forms.ValidationError("Русский перевод содержит недопустимые символы")
        return russian_translation
