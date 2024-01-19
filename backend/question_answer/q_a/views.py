# from django.views import View
from django.shortcuts import render
from .models import Question
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .forms import QAform
# from django.utils import timezone
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . serializers import Questionserializer

@api_view(['GET','POST'])
def Question_list(request,format=None):
    if request.method=='GET':
        questions=Question.objects.all()
        serializer=Questionserializer(questions,many=True)
        return Response(serializer.data)
   
    elif request.method=='POST':
        serializer=Questionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
@api_view(['GET','PUT','DELETE'])
def Question_detail(request,id,format=None):
    try:
       questions    =Question.objects.get(id=id)
    except Question.DoesNotExist:
        return Response(status=404)
    
    if request.method=='GET':
        serializer=Questionserializer(questions)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        
        serializer=Questionserializer(questions,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors,status=400)
    elif request.method=='DELETE':
        Question.delete()
        return Response(status=204)       
        
        

# class HomeView(View):

#     def get(self, request):
#         return render(request, 'home.html')

# class PythonView(View):
#     def get(self, request):
#         question_list = Question.objects.all().values()
#         content = {
#             "question_list": question_list
#         }
#         return render(request, 'python.html', content)
# class PythonansView(View):
#     def get(self,request,x_id):
#         ans_list=Question.objects.get(pk=x_id)
#         content={
#             "x":ans_list
#         }
#         return render(request,'pythonans.html',content)

# def QA_form(request):
#     form = QAform(request.POST or None)
#     if form.is_valid():
#         question = form.save(commit=False)  # Create an instance but don't save it yet
#         question.pub_date = timezone.now()  # Set the pub_date before saving
#         question.save()  # Save the instance with the pub_date set
#     context = {'form': form}
#     return render(request, "create.html", context)