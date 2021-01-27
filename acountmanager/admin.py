from django.contrib import admin
from .models import (
    User, 
    Donor, 
    DonorRecipient, 
    Organization,
)
# Register your models here.
admin.site.register(User)
admin.site.register(Donor)
admin.site.register(DonorRecipient)
admin.site.register(Organization)
