from django.urls import path
from . import views

urlpatterns = [
     path('', views.fees, name='fees'),
     path('submitform', views.payment_form, name='submitform'),
     path('success', views.success, name='success'),
     path('myfirst1/', views.fee_details, name='myfirst1'),
     path('fetch_data/', views.fetch_data, name='fetch_data'),
     path('show_data/<str:student_id>/<str:start_date>/<str:end_date>/', views.show_data, name='show_data'),
     path('download_pdf/<str:student_id>/<str:start_date>/<str:end_date>/', views.download_pdf, name='download_pdf'),
     # path('retrieve/', views.retrieve_payment_data, name='retrieve_payment_data'),

] 