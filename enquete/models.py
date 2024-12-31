import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Relacionamento
class Question(models.Model):
    # Métodos
    def __str__(self):
        return self.question_text
    

    def foi_publicado_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # Atributos
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    # Métodos
    def __str__(self):
        return self.choice_text


    # Atributos
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    