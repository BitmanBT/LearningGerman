# Generated by Django 5.2 on 2025-04-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('german_word', models.CharField(max_length=100, verbose_name='Немецкое слово')),
                ('russian_translation', models.CharField(max_length=100, verbose_name='Русский перевод')),
                ('difficulty', models.CharField(choices=[('A1', 'Начальный (A1)'), ('A2', 'Базовый (A2)'), ('B1', 'Средний (B1)'), ('B2', 'Выше среднего (B2)'), ('C1', 'Продвинутый (C1)')], default='A1', max_length=2, verbose_name='Уровень сложности')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'ordering': ['german_word'],
            },
        ),
    ]
