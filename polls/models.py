import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # test 고려 X
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # test, 날짜가 과거에 있을 때에만 True 반환
        now = timezone.now()
        return (now - datetime.timedelta(days=1) <= self.pub_date) and (self.pub_date <= now)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
