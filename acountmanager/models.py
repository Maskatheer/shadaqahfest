from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    DONOR = 1
    ORGANIZATION = 2
    RECIPIENT = 3

    ROLE_CHOICES = (
        (DONOR, 'Donor'),
        (ORGANIZATION, 'Organization'),
        (RECIPIENT, 'Recipient'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    

class Organization(models.Model):

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

    STATUS  = (
        ('verified', 'verified'),
        ('unverified', 'unverified'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    ktp_in_charge = models.CharField(max_length=16, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    handphone = models.CharField(max_length=20, blank=True, null=True)
    type_organization = models.CharField(
        max_length=50, choices=TYPE_ORG, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        choices=STATUS, max_length=20, default='unverified')

    def __str__(self):
        return self.organization_name

class Donor(models.Model):

    STATUS = (
        ('verified', 'verified'),
        ('unverified', 'unverified'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_location = models.CharField(max_length=100, blank=True, null=True)
    home_latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    home_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    ktp_id = models.CharField(max_length=16, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(
        choices=STATUS, max_length=20, default='unverified')

    def __str__(self):
        return self.user.username

class DonorRecipient(models.Model):

    JOB_STATUS = (
        ('Unemployed','Unemployed / Belum Bekerja'),
        ('Jobless', 'Jobless / Pengangguran'),
        ('Labor Force','Labor Force / Buruh'),
        ('Pedagang Asong' , 'Pedagang Asong'),
        ('Serabutan','Serabutan'),
        ('Farmer','Petani / Farmer'),
        ('Maid', 'ART / HouseMaid'),
        ('Marbot', 'Marbot'),
        ('Tukang Jahit', 'Tukang Jahit'),
        ('Cleaning Service', 'Cleaning Service'),
        ('Driver', 'Supir / Driver'),
        ('Sex Labour', 'Sex Labour / WTS / Pekerja Seks'),
    )

    MARITAL_STATUS = (
        ('Single', 'Single / Bujang'),
        ('Divorce-1', 'Divorce / Duda / Janda / Cerai Hidup'),
        ('Divorce-2', 'Divorce / Duda / Janda / Cerai Mati'),
        ('Polygamous', 'Polyginy'),
        ('Castrate', 'Castrate'),
    )

    FAMILY_STATUS = (
        ('Kepala Keluarga-1', 'Kepala Keluarga (ayah)'),
        ('Kepala Keluarga-2', 'Kepala Keluarga (ibu'),
        ('Anak', 'Anak'),
        ('Nenek', 'Nenek'),
        ('Kakek', 'Kakek'),
    )

    STATUS = (
        ('verified', 'verified'),
        ('unverified', 'unverified'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    ktp_id = models.CharField(max_length=16, blank=True, null=True)
    kk_id = models.CharField(max_length=16, blank=True, null=True)
    jobs = models.CharField(max_length=20, blank=True, null=True)
    job_status = models.CharField(
        max_length=50, choices=JOB_STATUS, blank=True, null=True)
    marital_status = models.CharField(
        max_length=50, choices=MARITAL_STATUS, blank=True, null=True)
    family_status = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    keluarga_tanggungan = models.IntegerField()
    birth_date = models.DateField()
    pengeluaran_per_bulan = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default = 'unverified')
    
    def __str__(self):
        return self.user.username