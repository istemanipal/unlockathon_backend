from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django import forms


from .models import CustomUser
# Register your models here.



class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('registration_number','phone','points','current_question','skips')}),
    )
    readonly_fields=['points','phone',]
    list_display=['username','first_name','last_name','points','current_question','skips']
    ordering=['points']

admin.site.register(CustomUser,MyUserAdmin)