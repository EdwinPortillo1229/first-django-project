from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])

    context = {
        'latest_question_list': lastest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")