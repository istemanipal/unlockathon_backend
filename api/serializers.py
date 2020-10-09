from rest_framework.serializers import ModelSerializer
from user.models import CustomUser
from game.models import (Question)


class UserSerializer(ModelSerializer):

    class Meta:
        model=CustomUser
        fields=['first_name','last_name','registration_number','email','phone','points','current_question','skips']


class QuestionSerializer(ModelSerializer):

    class Meta:
        model=Question
        fields=['question_number','question','image','hint']