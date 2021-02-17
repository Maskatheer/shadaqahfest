from django.shortcuts import render

# Create your views here.
def browse_view(request):
    return render(request, 'browse.html')