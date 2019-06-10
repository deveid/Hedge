from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate
from .models import User
from django.forms.widgets import SelectDateWidget
from .models import *

categories=(('Investor','Investor'),('Business Owner','Business Owner'))
gender=(('Male','Male'),('Female','Female'))

class RegistrationForm(UserCreationForm):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname=forms.CharField(max_length=50)
    username=forms.CharField(max_length=20)
    BirthDate=forms.DateField(widget=SelectDateWidget(years=range(1930,2018)))
    Gender=forms.ChoiceField(choices=gender)
    Category=forms.ChoiceField(choices=categories)
    phone_number = forms.CharField(max_length=15, required=True)
    
    
    
    class Meta:
        model = User
        fields = ('username', 'phone_number','fullname','BirthDate','Gender','Category', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        user.fullname = self.cleaned_data['fullname']
        user.BirthDate = self.cleaned_data['BirthDate']
        user.Gender = self.cleaned_data['Gender']
        user.Category = self.cleaned_data['Category']

        #user.is_verified = False
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            
        return user
    
class VerificationForm(forms.Form):
    token_number = forms.IntegerField(required=True)
    
    class Meta:
        fields = ('token_numer')
        
    def getToken(self):
        self.full_clean()
        return self.cleaned_data['token_numer']


class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('User does not exists')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(loginform,self).clean(*args,**kwargs)


class Investor_form(forms.ModelForm):

    class Meta:
        model=Investor_Registration
        fields=("__all__")
        exclude=['owner','Investment','Earnings','investedCompanyName','noOfCompanyInvested']

class Business_owner_form(forms.ModelForm):
    
    class Meta:
        model=BusinessOwner_Registration
        fields=("__all__")
        exclude=['owner','verifyDocument','Investment','RepaidInvestment','InvestorName','noOfInvestor']

class payment_form(forms.ModelForm):

    class Meta:
        model=payments
        fields=('Amount','figiID','Bank_Teller')
        exclude=['paid']

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model=ContactModel
        fields=("__all__")
        


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     subject=forms.CharField(max_length=200)
#     message = forms.CharField(widget=forms.Textarea)