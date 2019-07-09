from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, VerificationForm
from .models import User
import urllib.request
import matplotlib.pyplot as plt
from django.template import RequestContext
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView,TemplateView
import firebase
from django.contrib.auth.mixins import LoginRequiredMixin
import random
import requests
from matplotlib import pylab
from pylab import *
import mpld3
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Initialize Firebase


# Create your views here.
def firstpage(request):
    return render(request, 'index.html')

# def contactus(request):
#     contform=ContactForm()
#     if request.method=='POST':
#         contform=ContactForm()
#         if contform.is_valid():
#             contform.save()
#             # sender_name = form.cleaned_data['name']
#             # sender_email = form.cleaned_data['email']
#             # sender_subject=form.cleaned_data['subject']
#             # message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
#             # send_mail('New Enquiry', message, sender_email, ['deveidtolu18@gmail.com.com'])
#             return redirect('Nittan:success')
#     else:
#         contform=ContactForm()

#     return render(request,'contact.html',{'form':contform})

class CreateMyModelView(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('success')
    context_object_name = 'contact'

class successemail(TemplateView):
    template_name = 'success.html'
    context_object_name = 'success'

def aboutus(request):
    return render(request,'about.html')

def loginview(request):
    
    if request.method == 'POST':
        lform=loginform(request.POST)
        if lform.is_valid():
            username=lform.cleaned_data.get('username')
            password=lform.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user.has_filledform==False:
                cuurentUser=User.objects.get(username=username)
                print(User.objects.get(username=username).fullname)
                if cuurentUser.Category=='Investor':
                    login(request,user)
                    return redirect('Nittan:detailinvestor')
                elif cuurentUser.Category=='Business Owner':
                    login(request,user)
                    return redirect('Nittan:detailbusiness')
            else:
                cuurentUser=User.objects.get(username=username)
                if cuurentUser.Category=='Investor':
                    login(request,user)
                    return redirect('Nittan:dashboardinvestor')
                elif cuurentUser.Category=='Business Owner':
                    login(request,user)
                    return redirect('Nittan:dashboardbusiness')
    lform=loginform()
    context={'lform':lform}
    return render(request,'login.html',context)

 
def otp_register(request):
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            phone_number = regform.cleaned_data.get('phone_number')
            user=regform.save()
            if user.id:
                api_key='7257c278-4852-11e9-8806-0200cd936042'
                OTP_VALUE=random.choice(range(1000,9999))
                first_url = "https://2factor.in/API/V1/"
                api=first_url+api_key
                url=api+'/SMS/'+'234'+phone_number+'/AUTOGEN'+'/OTPSEND'
                response = requests.get(url)
                response = requests.request("GET", url)
                data = response.json()
                request.session['otp_session_data'] = data['Details']
                print(data)
                print(request)
                # otp_session_data is stored in session.
                response_data = {'Message':'Success'}  
                user = regform.save()             
                return redirect('Nittan:login')
    else:
        regform = RegistrationForm()
    context = {}
    # context.update(request)
    context['regform'] = regform
    return render(request, 'signup.html', context)

def verifyview(request):
    vform=VerificationForm()
    if request.method == 'POST':
        vform = VerificationForm(request.POST)
        if vform.is_valid():
            token = vform.cleaned_data.get('token_number')
            url="http://2factor.in/API/V1/7257c278-4852-11e9-8806-0200cd936042/SMS/VERIFY/"+request.session['otp_session_data']+'/'+str(token)
            # otp_session_data is fetched from session.
            print(url)
            response = requests.request("GET", url)
            data = response.json()
            print(response)
            print(data)
            if data['Status'] == "Success":
                logged_user.is_active = True
                response_data = {'Message':'Success'}
                return render(request, 'login.html')
            else:
                    response_data = {'Message':'Failed'}

        else:
            vform=VerificationForm()
    return render(request,'verify.html',{'vform':vform})



def details_business(request):
    if request.user.is_authenticated:
        business_form=Business_owner_form()
        if request.method=='POST':
            business_form=Business_owner_form(request.POST,request.FILES)
            if business_form.is_valid():
                bform=business_form.save()
                bform.per=request.user
                bform.owner=request.user
                bform.save()
                request.user.has_filledform=True
                request.user.save()
                return redirect('Nittan:dashboardbusiness')
        context={}
        context['Bform']=business_form
        return render(request,'businessSheet.html',context)
    else:
        return redirect('Nittan:login')

def details_investor(request):
    if request.user.is_authenticated:
        Iform=Investor_form()
        if request.method=='POST':
            Invest_form=Investor_form(request.POST)
            if Invest_form.is_valid():
                Iform=Invest_form.save()
                request.user.has_filledform=True
                request.user.save()
                return redirect('Nittan:dashboardinvestor')
        context={}
        context['Iform']=Iform
        return render(request,'investSheet.html',context)
    else:
        return redirect('Nittan:login')


def business_to_invest(request):
    allDocs = BusinessOwner_Registration.objects.all()[4:]#prints starting from the fourth
    context={"all":allDocs}
    return render(request,'invest.html',context=context)


def investor_dashboard(request):
    if request.user.is_authenticated:
        investment = Investor_Registration.objects.filter(owner=request.user).values().all()
        allDocs = BusinessOwner_Registration.objects.all()
        earningsAmount=list(Investor_Registration.objects.filter(owner=request.user).values_list('Earnings',flat=True))
        companyName=list(Investor_Registration.objects.filter(owner=request.user).values_list('investedCompanyName',flat=True))
        companyName=list([str(x) for x in companyName[0].split(',')])
        earningsAmount=list([int(x) for x in earningsAmount[0].split(',')])
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(companyName,earningsAmount,color='teal')
        plt.xticks(companyName,companyName)
        plt.xlabel('Invested Businesses')
        plt.ylabel('Amount of Earnings (Naira)')
        html_fig = mpld3.fig_to_html(fig,template_type='general')
        plt.close(fig)
        pDetail=payment_form()
        if request.method=='POST':
            pDetail=payment_form(request.POST,request.FILES)
            if pDetail.is_valid():
                pDetail.save()
                return HttpResponse('Success! Your Payment Detail will be Processed within the next 24hours')
        context={'doc':allDocs,'pDetail':pDetail,'iDetail':investment,'div_figure' : html_fig}
        return render(request,'dashboardinvestor.html',context)
    else:
        return redirect('Nittan:login')


def business_dashboard(request):
    if request.user.is_authenticated:
        context = RequestContext(request)
        reg = BusinessOwner_Registration.objects.filter(owner=request.user).values().all()
        InvestorName=list(BusinessOwner_Registration.objects.filter(owner=request.user).values_list('InvestorName',flat=True))
        investmentAmount=list(BusinessOwner_Registration.objects.filter(owner=request.user).values_list('Investment',flat=True))
        investmentAmount=list([int(x) for x in investmentAmount[0].split(',')])
        InvestorName=list([str(x) for x in InvestorName[0].split(',')])
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(InvestorName,investmentAmount,color='teal')
        plt.xticks(InvestorName,InvestorName)
        plt.xlabel('Investor')
        plt.ylabel('Amount of Investment (Naira)')
        html_fig = mpld3.fig_to_html(fig,template_type='general')
        plt.close(fig)
        reg1 =BusinessOwner_Registration.objects.filter(owner=request.user).values_list('verifyDocument',flat=True)
        stat=reg1[0]
        if stat==False:
            das='Not Verified'
        else:
            das='Verified'
        context={"obj":reg,'stat':das,'div_figure' : html_fig}
        return render(request,'dashboardbusiness.html',context)
    else:
        return redirect('Nittan:login')

def businessDocument(request):
    if request.user.is_authenticated:
        context = RequestContext(request)
        reg = BusinessOwner_Registration.objects.filter(owner=request.user).values().all()
        context={"obj":reg}
        return render(request,'documents.html',context)
    else:
        return redirect('Nittan:login')

def verifiedbusiness(request):
    if request.user.is_authenticated:
        pDetail=payment_form()
        amt=pDetail['Amount'].value()
        if request.method=='POST':
            amt=pDetail['Amount'].value()
            context={'amt':amt}
            pDetail=payment_form(request.POST,request.FILES)
            #amt=request.POST.get("Amount")
            if pDetail.is_valid():
                pDetail.save()
                return HttpResponse('Success! Your Payment Detail will be Processed within the next 24hours')
        amt=pDetail['Amount'].value()
        context = RequestContext(request)
        verified = BusinessOwner_Registration.objects.filter(verifyDocument=True).values().all()
        context={"verf":verified,'pDetail':pDetail,'amt':amt}
        return render(request,'verified.html',context)
def logoutview(request):
    logout(request)
    request.session.flush()
    request.user = User
    return render(request,'index.html')


