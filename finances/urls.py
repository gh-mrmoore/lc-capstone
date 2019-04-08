#urls for the 'finances django app

from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('banks', views.BanksView.as_view(), name='accounts'), 
    path('banks/<int:bank_id>', views.bank_detail, name='acct_details'), 
    path('transactions', views.TransactionView.as_view(), name='transacts'), 
    #switching to function-based views since class-based
    #form views are eluding me at the moment
    #path('transactions/add', views.addline, name='line-add'), 
    path('transactions/add/<int:bank_id>/', views.addline, name='line-update'), 
    path('transactions/edit/<int:line_id>/', views.editline, name='line-edit'), 
]