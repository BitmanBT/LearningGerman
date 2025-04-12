"""This module is responsible for the data models stored in the database."""
from django.db import models
from django.core.validators import MinLengthValidator


class Word(models.Model):
    """
    The model of words stored in the database

    Attributes:
        DIFFICULTY_CHOICES (list[tuple[str, str]]): word complexity options in German
        german_word (CharField[str]): a word in German
        russian_translation (CharField[str]): translation of a German word into Russian
        difficulty (CharField[str]): Common difficulty of a word in German
    """
    DIFFICULTY_CHOICES = [
        ('A1', 'Начальный (A1)'),
        ('A2', 'Базовый (A2)'),
        ('B1', 'Средний (B1)'),
        ('B2', 'Выше среднего (B2)'),
        ('C1', 'Продвинутый (C1)'),
    ]
    german_word = models.CharField(max_length=100, verbose_name="Немецкое слово")
    russian_translation = models.CharField(max_length=100, verbose_name="Русский перевод")
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY_CHOICES, default='A1',
                                  verbose_name="Уровень сложности")
    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['german_word']

    def __str__(self):
        return f"{self.german_word} - {self.russian_translation}"

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('bug', 'Сообщение об ошибке'),
        ('suggestion', 'Предложение по улучшению'),
        ('question', 'Вопрос'),
        ('other', 'Другое'),
    ]
    
    feedback_type = models.CharField(
        'Тип обращения',
        max_length=20,
        choices=FEEDBACK_TYPES,
        default='suggestion'
    )
    email = models.EmailField('Email для ответа', blank=True, null=True)
    message = models.TextField(
        'Сообщение',
        validators=[MinLengthValidator(10, "Сообщение должно содержать минимум 10 символов")]
    )
    consent = models.BooleanField(
        'Согласие на обработку данных',
        default=False
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_feedback_type_display()} от {self.created_at.strftime('%Y-%m-%d %H:%M')}"
