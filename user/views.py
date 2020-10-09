from django.shortcuts import render,redirect,reverse
from .forms import CustomUserCreationForm
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def index(request):
    print(timezone.localtime(timezone.now()).date())

    return render(request,'user/index.html')

def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,f'Registered Successfully under registration number {user.registration_number}')
            return redirect(reverse('user:login'))
        else:
            messages.error(request,'Check filled data',extra_tags='danger')
        context={
            'form':form
        }

        return render(request,'user/register.html',context=context)

    form=CustomUserCreationForm()
    context={'form':form}
    return render(request,'user/register.html',context=context)