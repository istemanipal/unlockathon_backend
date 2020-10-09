from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth import get_user_model
from .models import Question
# Create your views here.

from django.utils import timezone

@login_required
def index (request):
    # try:
    #     question=Question.objects.get(question_number=request.user.current_question)
    # except:
    #     return redirect(reverse("game:end"))
    # contacts=get_user_model().objects.filter(is_staff=True)
    # leaderboard=get_user_model().objects.filter(is_staff=False).order_by('-points')
    # context={
    #     'question':question,
    #     'toppers':leaderboard,
    #     'contacts':contacts,

    # }
    return render(request,"game/react_html.html")



@login_required
def check_answer(request):
    if request.method=='POST':
        question=Question.objects.get(question_number=request.user.current_question)
        if question.answer.lower().replace(" ","") == request.POST.get('ans').lower().replace(" ",""):
            request.user.current_question+=1
            request.user.points+=3
            request.user.save()
            return HttpResponse("correct")
        else:
            return HttpResponse("wrong")
    
    else:
        return HttpResponseBadRequest("Not allowed")

@login_required
def skip_question(request):
    if request.method=='POST':
        correct_answer=Question.objects.get(question_number=request.user.current_question).answer
        request.user.current_question+=1
        request.user.save()
        return HttpResponse(correct_answer)
    else:
        return HttpResponseBadRequest("Not allowed")


@login_required
def game_end(request):
    if request.user.current_question<=Question.objects.all().count():
        return redirect(reverse("game:index"))
    
    return render(request,"game/end.html")