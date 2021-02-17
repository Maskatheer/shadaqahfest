from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.
def login_view(request):
    context = {

    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                print('user bener')
                login(request, user)
                return redirect('home')
            else:
                print('eror user none')
    else:
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context=context)
    

def register_view(request):
    return render(request, 'register.html')

def register_organization(request):
    return render(request, 'register_org.html')

def register_recipient(request):
    return render(request, 'register_recipient.html')

def register_donor(request):
    return render(request, 'register_donor.html')

def profile(request):
    return render(request, 'profile.html')

