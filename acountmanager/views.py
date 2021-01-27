from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_organization(request):
    return render(request, 'register_org.html')

def register_recipient(request):
    return render(request, 'register_recipient.html')

def register_donor(request):
    return render(request, 'register_donor.html')

def profile(request):
    return render(request, 'profile.html')

