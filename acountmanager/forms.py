from django import forms
from django.contrib.auth.forms import UserCreationForm
from acountmanager.models import User

class OrganizationRegForm(UserCreationForm):

    TYPE_ORG = (
        ('Masjid', 'Masjid / Mosque'),
        ('Orphanage', 'Panti Asuhan / Orphanage'),
        ('Human Social Welfare', 'Social Welfare'),
        ('Animal Social Welfare', 'Animal Social Welfare'),
        ('Educational Institution', 'Education Institution/Community'),
        ('People Community', 'People Community'),
        ('Religious Community', 'Religious Community'),
        ('Religious Organization', 'Religious Organization'),
        ('Sport Association', 'Sport Association'),
        ('Sport Community', 'Sport Community/Organization'),
        ('CSR', 'Community Social Responsibility'),
        ('Other', 'Other'),
    )

    organization_name = forms.CharField(help_text='Required')
    address = forms.CharField(help_text='Address')
    latitude_longitude = forms.CharField(help_text='Latitude Longitude')
    ktp_id = forms.CharField(help_text='Required for activation')
    telephone = forms.CharField(help_text='Office Number')
    handphone = forms.CharField(help_text='Handphone')
    type_organization = forms.ChoiceField(choices=TYPE_ORG, required=False)
    description = forms.TextField()

    class Meta:
        model = User
        field = ('username', 'email', 'organization_name', 'ktp_id', 'type_organization', 'address', 'telephone', 'description','password1', 'password2')