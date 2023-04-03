from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255, unique=True, default='a', null=True)
    pub_date = models.DateTimeField('Date published', null=True)

    def __str__(self) -> str:
        return self.text
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    is_true = models.BooleanField(default = False)


    def __str__(self) -> str:
        return f"{self.question} - {self.text} - {self.is_true}"    