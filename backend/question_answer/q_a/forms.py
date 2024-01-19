from django import forms
from .models import Question

class QAform(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ['question_txt','answer','exp_sol'
        ]