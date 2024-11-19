from django.urls import path 
from . import views

urlpatterns=[
    path('cv/',views.Contact_API.as_view()),
    path('ev/',views.Educationdetail_API.as_view()),
    path('fv/',views.Familydetails_API.as_view()),
    path('pv/',views.Partnerprefarencedetails_API.as_view()),
    path('cv/<int:pk>/',views.Contact_API.as_view()),
    path('ev/<int:pk>/',views.Educationdetail_API.as_view()),
    path('fv/<int:pk>/',views.Familydetails_API.as_view()),
    path('pv/<int:pk>/',views.Partnerprefarencedetails_API.as_view())
]