"""This module is responsible for the forms that the application uses"""
from django import forms
from .models import Word, Feedback

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

class FeedbackForm(forms.ModelForm):
    consent = forms.BooleanField(
        label='Я согласен на обработку персональных данных',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'email', 'message', 'consent']
        widgets = {
            'feedback_type': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Опишите вашу проблему или предложение...'
            }),
        }
        labels = {
            'feedback_type': 'Тип обращения',
            'email': 'Ваш email (необязательно)',
            'message': 'Сообщение',
        }
