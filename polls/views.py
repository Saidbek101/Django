from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    questions = Question.objects.all()
    # response = ''
    # for question in questions:
    #     response += f"{questions.text}\n"

    # return HttpResponse('Question list here.<br>{response}')

    context = {
        'questions': questions
    }
    return render(request, 'question.html', context = context)
   

def question_detail(request, pk):
     try:
        question = Question.objects.get(id=pk)
     except Question.DoesNotExist:
        return HttpResponse('Not found !!')

     return HttpResponse(f"Question text: {question.text},<br>desription: {question.pub_date}")