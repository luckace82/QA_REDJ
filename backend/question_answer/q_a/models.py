from django.db import models

class Question(models.Model):
    question_txt=models.CharField(max_length=1000)
    pub_date=models.DateTimeField("published_date")
    exp_sol=models.TextField(max_length=1000,default="____")
    answer=models.TextField(max_length=1000,default="____")
    def __str__(self):
        return f"{self.question_txt},{self.exp_sol},{self.answer}"
        
    


