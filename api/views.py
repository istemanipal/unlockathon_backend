from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



from .serializers import UserSerializer,QuestionSerializer


from game.models import Question
# Create your views here.

def get_user(request):
    return request.user

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_logged_in_user(request):
    user=get_user(request)
    serializer=UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question(request):
    context={}
    try:
        question=Question.objects.get(question_number=get_user(request).current_question)
        context['status']='found'
        serializer=QuestionSerializer(question)
        context['question']=serializer.data
    except:
        context['status']='not found'
        context['question']=None
        context['message']="Congratutlations! You have completed all questions!"
    
    return Response(context)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leaderboard(request):
    context={}
    leaderboard=get_user_model().objects.filter().order_by('-points')
    
    if leaderboard.count()>0:
        serializer=UserSerializer(leaderboard,many=True)
        context['status']='found'
        context['leaderboard']=serializer.data
    
    else:
        context['status']='not found'
        context['leaderboard']=[]
    
    return Response(context)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_answer(request):
    context={}

    answer=request.POST.get('answer')
    user=get_user(request)
    if answer.lower().replace(" ","") == Question.objects.get(question_number=user.current_question).answer.lower().replace(" ",""):
        try:
            user.current_question+=1
            user.points+=1
            context['points']=user.points
            user.save()
            context['status']='correct'

            try:
                next_question=Question.objects.get(question_number=user.current_question)
                serializer=QuestionSerializer(next_question)
                context['next_question']=serializer.data
            except:
                context['next_question']=None
                context['message']='Congratulations! You have completed all questions!'

            
        except:
            context['status']='Something Went Wrong'
       
    else:
        context['status']='wrong'
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def skip(request):
    context={}
    user=get_user(request)
    if user.skips <=0:
        context['status']='insufficient skips'
        return Response(context)
    try:
        user.current_question+=1
        user.skips-=1
        user.save()
        try:
            next_question=Question.objects.get(question_number=user.current_question)
            serializer=QuestionSerializer(next_question)
            context['next_question']=serializer.data
        except:
            context['next_question']=None
            context['message']='Congratulations! You have completed all questions!'
        
        context['status']='successful'
        context['skips']=user.skips
    
    except:
        context['status']='Something went wrong'
    
    return Response(context)
    

        

