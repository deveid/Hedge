from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.models import  User
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from django.core.validators import MaxValueValidator

# Create your models here.
gender=(('Male','Male'),('Female','Female'))
typeBank=(('Savings','Savings'),('Current','Current'))
stage=(('Idea','Idea'),('Market-Testing','Market-Testing'),('Deployed','Deployed'))
industry=(('Trading','Trading'),('ICT','ICT'),('Real Estate','Real Estate'))
period=(('12months','12months'),('18months','18months'),('24months','24months'),('36months','36months'),('60months','60months'))
categories=(('Investor','Investor'),('Business Owner','Business Owner'))
gender=(('Male','Male'),('Female','Female'))


# class MaxSizeValidator(MaxValueValidator):
#     message = ('The file exceed the maximum size of %(limit_value)s MB.')
#     def __call__(self, value):
#         # get the file size as cleaned value
#         cleaned = self.clean(value.size)
#         params = {'limit_value': self.limit_value, 'show_value': cleaned, 'value': value}
#         if self.compare(cleaned, self.limit_value * 1024 * 1024): # convert limit_value from MB to Bytes
#             raise ValidationError(self.message, code=self.code, params=params)


class User(AbstractUser):
    
    phone_number = models.CharField(('phone number'), max_length=15,default='+234',
        help_text=('Field to save the phone number of the user.'),unique=True)
    fullname=models.CharField(max_length=50)
    is_verified = models.BooleanField(('verified'), default=False,
        help_text=('Designates whether this user should be treated as '
                    'verified.'))
    has_filledform=models.BooleanField(default=False)
    Gender=models.CharField(choices=gender,max_length=20)
    Category=models.CharField(choices=categories,max_length=20)


    def full_name(self):
        return self.fullname

    def cat(self):
        return self.Category

class Investor_Registration(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    investor_fullname=models.CharField(default="Jon Samuel",max_length=50,null="True")
    Address=models.TextField(default='Resendential Address')
    Age=models.IntegerField()
    Gender=models.CharField(choices=gender,max_length=50)
    Figi_Username=models.CharField(default='Figi Username',blank=True,max_length=50)
    Next_of_Kin=models.CharField(default='Next of kin Name',max_length=50)
    Next_of_Kin_Address=models.TextField(default='Address of Next of kin',max_length=100)
    Bank_Name=models.CharField(default='GTB',max_length=50)
    Bank_Type=models.CharField(choices=typeBank,max_length=50)
    Account_Number=models.IntegerField(default='2091047681')
    Bvn=models.IntegerField(help_text=('Enter your bank BVN'))
    Investment=models.IntegerField(default=000000)
    Earnings=models.CharField(default='0',max_length=900000000000000000000000000000)
    investedCompanyName=models.CharField(default='None',max_length=90000000000000000)
    noOfCompanyInvested=models.IntegerField(default=0)
    
    def __str__(self):
            return self.investor_fullname

class BusinessOwner_Registration(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Phone_Number=models.IntegerField(default='09036878432',unique=True)
    Figi_ID=models.IntegerField(blank=True)
    Bvn=models.IntegerField()
    Business_Image=models.ImageField(upload_to='media/')
    CAC_certificate=models.ImageField(upload_to='media/')
    Affidavit=models.ImageField(upload_to='media/')
    Guarrantor1_Email=models.CharField(default='Gurrantor Email',max_length=50)
    Guarrantor1_Phone_Number=models.IntegerField(default='09032421311')
    Guarrantor2_Email=models.CharField(default='Gurrantor Email',max_length=50)
    Guarrantor2_Phone_Number=models.IntegerField(default='09032421311')
    Present_Stage_of_Business=models.CharField(choices=stage,max_length=50)
    Passport_Photograph=models.ImageField(upload_to='media/')
    Business_Statement=models.TextField(default='Tell us about your Business')
    Business_Video=models.FileField(upload_to='media',help_text="Video size should not be more than 2MB")
    Name_of_Business=models.CharField(default='Business Name',max_length=50)
    Industry_of_Business=models.CharField(choices=industry,max_length=50)
    Address_of_Business=models.TextField(default='Business Address',max_length=100)
    Percent=models.FloatField(help_text='How much percent are you willing to give',default=5)
    verifyDocument=models.BooleanField(default=False)
    Time_Period=models.IntegerField(default=6,help_text=('Time Period of Investment in months'))
    Investment=models.CharField(default=0,max_length=90000000000000000000000000000000)
    RepaidInvestment=models.IntegerField(default=000000)
    InvestorName=models.CharField(default='None',max_length=90000000000000000)
    noOfInvestor=models.IntegerField(default=0)

    def __str__(self):
            return str(self.Phone_Number)

class payments(models.Model):
    Amount=models.IntegerField(default=00000)
    figiID=models.CharField(default='F-00000',max_length=10)
    Bank_Teller=models.ImageField(upload_to='media/',default='/no Image Uploaded')
    expectedEarning=models.CharField(max_length=2000)
    paid=models.BooleanField(default=False)


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=9000000000000000000000000)
    def __str__(self):
            return str(self.name)