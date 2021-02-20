from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .forms import LoginForm, IndividualRegForm, OrganizationRegForm
from .models import User, Organization, Donor

# Create your views here.

    

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    return render(request, 'register.html')

def register_organization(request):
    if request.method == 'POST':
        form = OrganizationRegForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            # form.username=form.cleaned_data['organization_username']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            new_user = User.objects.create(username=username, email=email, password=password1)
            organization_name = form.cleaned_data['organization_name']
            address = form.cleaned_data['address']
            ktp_id = form.cleaned_data['ktp_id']
            telephone = form.cleaned_data['telephone']
            handphone = form.cleaned_data['handphone']
            type_organization = form.cleaned_data['type_organization']
            description = form.cleaned_data['description']
            
            new_organization = Organization.objects.create(
                user = new_user,
                organization_name = organization_name,
                address = address,
                ktp_in_charge = ktp_id, 
                telephone = telephone,
                handphone = handphone,
                type_organization = type_organization,
                description = description
            )
            login(request, new_user)
            return redirect('home')
        else:
            form = OrganizationRegForm(request.POST, initial=request.POST)
            context = {
                'form': form
            }
            return render(request, 'register_org.html', context=context)
    else:
        form = OrganizationRegForm()
        context = {
            'form':form
        }
        return render(request, 'register_org.html', context=context)
        

def register_recipient(request):
    return render(request, 'register_recipient.html')

def register_donor(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'POST':
        form = IndividualRegForm(request.POST)
        print('preketek')
        if form.is_valid():
            print('valid')
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            password1 = form.cleaned_data['password1']
            new_user = User.objects.create(username = username, email=email, password=password1)
            new_donor = Donor.objects.create(user=new_user)
            print('berhasil')
            login(request, new_user)
            return redirect('home')
        else:
            form = IndividualRegForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'register_donor.html', context=context)
    else:
        form = IndividualRegForm()
        context = {
            'form':form
        }
        return render(request, 'register_donor.html', context=context)
        

def profile(request):
    return render(request, 'profile.html')

