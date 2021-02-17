from django.urls import path
from .views import register_view, register_donor, register_organization, register_recipient
urlpatterns = [
    path('', register_view, name='register'),
    path('donor/', register_donor, name='register_donor'),
    path('organization/', register_organization, name='register_organization'),
    path('recipient/', register_recipient, name='register_recipient'),

]
