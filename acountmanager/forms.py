from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from acountmanager.models import User

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class OrganizationRegForm(forms.Form):

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

    organization_name = forms.CharField(help_text='Required', required=True)
    username = forms.CharField(
        help_text='Required', required=True, label='Organization Username')
    address = forms.CharField(help_text='Address', required=True)
    email = forms.EmailField(help_text='Email Adress')
    # latitude_longitude = forms.CharField(help_text='Latitude Longitude', required=False)
    ktp_id = forms.CharField(
        help_text='Required for activation', required=True)
    telephone = forms.CharField(help_text='Office Number')
    handphone = forms.CharField(help_text='Handphone', required=True)
    type_organization = forms.ChoiceField(choices=TYPE_ORG, required=False)
    description = forms.CharField(max_length=10000, widget=forms.Textarea, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    error_messages = {
        'password_mismatch':'The two password fields didn’t match.',
        'username_taken': 'Username already taken, please use other.',
    }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        exist_user_with_username = User.objects.filter(username=username)

        if len(exist_user_with_username) == 0:
            pass
        else:
            print(exist_user_with_username)
            raise ValidationError(
                self.error_messages['username_taken'],
                code='username_taken',
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class IndividualRegForm(forms.Form):

    email = forms.EmailField(help_text='Email Text', required='True')
    username = forms.CharField(help_text='Username', required='True')
    full_name = forms.CharField(help_text='Your Real Name', required='True')
    password1 = forms.CharField(label="Password",
                                strip=False,
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'new-password'}),
                                help_text=password_validation.password_validators_help_text_html(),)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'new-password'}),
                                strip=False,
                                help_text="Enter the same password as before, for verification.")

    error_messages = {
        'password_mismatch':'The two password fields didn’t match.',
        'username_taken': 'Username already taken, please use other.',
    }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        exist_user_with_username = User.objects.filter(username=username)

        if len(exist_user_with_username) == 0:
            pass
        else:
            print(exist_user_with_username)
            raise ValidationError(
                self.error_messages['username_taken'],
                code='username_taken',
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2





