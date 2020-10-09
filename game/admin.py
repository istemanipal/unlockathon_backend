from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=['question_number','question','answer']
    ordering=['question_number']


admin.site.register(Question,QuestionAdmin)