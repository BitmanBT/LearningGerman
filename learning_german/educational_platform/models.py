from django.db import models

class Word(models.Model):
    DIFFICULTY_CHOICES = [
        ('A1', 'Начальный (A1)'),
        ('A2', 'Базовый (A2)'),
        ('B1', 'Средний (B1)'),
        ('B2', 'Выше среднего (B2)'),
        ('C1', 'Продвинутый (C1)'),
    ]
    
    german_word = models.CharField(max_length=100, verbose_name="Немецкое слово")
    russian_translation = models.CharField(max_length=100, verbose_name="Русский перевод")
    difficulty = models.CharField(
        max_length=2, 
        choices=DIFFICULTY_CHOICES, 
        default='A1',
        verbose_name="Уровень сложности"
    )

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['german_word']

    def __str__(self):
        return f"{self.german_word} - {self.russian_translation}"