from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ioneu'

urlpatterns = [
    # 1. urls 생성
    path('main/wealfare/<str:hashtag>', views.WelfareCompany), # ioneu > views.py 에 있는 index 호출
    path('main/financePolicy', views.FinancePolicy),
    path('main/Policy/<str:hashtag>', views.CompanyPolicy)
]
