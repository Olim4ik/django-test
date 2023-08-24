import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(verbose_name="Текст вопроса", max_length=200)
    pub_date = models.DateTimeField(verbose_name="Дата публикации")
    
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name="Текст Варианта", max_length=200)
    votes = models.IntegerField(verbose_name="Число голосов", default=0)
    
    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

