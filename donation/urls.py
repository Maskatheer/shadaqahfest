from django.urls import path
from .views import browse_view

urlpatterns = [
    path('home/', browse_view, name='home')
]
