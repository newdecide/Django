from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.views.generic import ListView, DetailView # 사용시 문법이 구조화 된다,

# rest API import
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .seriallizers import QuestionSeriallizer

class ApiQiestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSeriallizer


class ApiQuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSeriallizer


# 클래스용
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'

# vote는 뷰가 아니기 때문에 클래스나 함수나 동일하다.
def vote(request, request_id):
    question = get_object_or_404(Question, pk=request_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect('/polls/result/' + str(question.id))