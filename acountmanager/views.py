from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .forms import LoginForm, IndividualRegForm, OrganizationRegForm

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
                form = LoginForm()
    else:
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context=context)
    

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    return render(request, 'register.html')

def register_organization(request):
    if request.method == 'POST':
        form = OrganizationRegForm(request.POST)
    else:
        form = OrganizationRegForm()
        context = {
            'form':form
        }
        return render(request, 'register_org.html', context=context)
        

def register_recipient(request):
    return render(request, 'register_recipient.html')

def register_donor(request):
    if request.method == 'POST':
        form = IndividualRegForm(request.POST)
    else:
        form = IndividualRegForm()
        context = {
            'form':form
        }
        return render(request, 'register_donor.html', context=context)
        

def profile(request):
    return render(request, 'profile.html')

