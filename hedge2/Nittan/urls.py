from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,re_path
from . import views

urlpatterns = [
                    path(r'index', views.firstpage, name='index'),
                    path('about/', views.aboutus, name='about'),
                    path('sent/', views.successemail.as_view(), name='success'),
                    url(r'^contact/$', views.CreateMyModelView.as_view(), name='contact'),
                    # path('signup/', views.signupview, name='signup'),
                    # path('login/', views.loginview, name='login'),
                    url(r'^register/$', views.otp_register, name='register'),
                    url(r'^login/$', views.loginview, name='login'),
                    url(r'^verify/$', views.verifyview, name='verify'),
                    url(r'^detailbusiness/$', views.details_business,name='detailbusiness'),
                    url(r'^detailinvestor/$', views.details_investor,name='detailinvestor'),
                    url(r'^invest/$',views.business_to_invest,name='invest'),
                    url(r'^dashboardinvestor/$',views.investor_dashboard,name='dashboardinvestor'),
                    url(r'^dashboardbusiness/$',views.business_dashboard,name='dashboardbusiness'),
                    url(r'^documents/$',views.businessDocument,name='documents'),
                    url(r'^verifiedbusiness/$',views.verifiedbusiness,name='verified'),
                    url(r'^', views.logoutview, name='logout'),
                    # url(r'^business$', views.CreateMyModelView.as_view(), name='business'),
                    # url(r'^investor$', views.CreateInvestorView.as_view(), name='investor'),
                    # url(r'^status/$', views.otp_status, name='status'),
                    # url(r'^logout/$', views.otp_logout, name='logout'),
                    # url(r'^token/$', views.otp_token, name='token'),
                    


]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 