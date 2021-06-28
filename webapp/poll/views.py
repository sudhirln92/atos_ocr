from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http.response import   HttpResponse
from django.http import Http404
from poll.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'poll'
    context['questions'] = questions
    return render(request,'poll/index.html',context)

@login_required(login_url='/login/')
def details(request,id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request,'poll/details.html',context)

@login_required(login_url='/login/')
def poll(request,id=None):
    if request.method == 'GET':
        context = {}
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context['question'] = question
        return render(request,'poll/poll.html',context)
    if request.method == 'POST':
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id =user_id,choice_id=data['choice'])
        if ret:
            return HttpResponse('Your vote casted')
        else:
            return HttpResponse('Your vote is not done')