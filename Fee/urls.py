from django.urls import path
from . import views

urlpatterns = [
     path('', views.fees, name='fees'),
     path('submitform', views.payment_form, name='submitform'),
     path('success', views.success, name='success'),
     path('myfirst1/', views.fee_details, name='myfirst1'),

]