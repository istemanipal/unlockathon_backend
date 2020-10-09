from django.urls import path
from . import views



app_name="api"

urlpatterns=[

    path('get_logged_in_user',views.get_logged_in_user,name='logged_in_user'),
    path('get_question',views.get_question,name="get_question"),
    path('leaderboard',views.leaderboard,name="leaderboard"),
    path('check_answer',views.check_answer,name="check_answer"),
    path('skip',views.skip,name="skip"),

]