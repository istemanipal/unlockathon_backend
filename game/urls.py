from django.urls import path,include
from . import views

app_name="game"

urlpatterns = [
    path('',views.index,name="index"),
    path('check_answer',views.check_answer,name="check_answer"),
    path("skip",views.skip_question,name="skip"),
    path("end",views.game_end,name="end")
]