#urls for the 'kids' django app

from django.urls import path
from . import views

app_name = 'kids'
urlpatterns = [
    path('', views.index, name='index'), 
    path('add/<int:kid>', views.add, name='add'), 
    path('detail/<int:kid>', views.detail, name='detail'), 
    path('edit/<int:event>', views.edit, name='edit')
    #moving away from class-based views for the moment
    #path('', views.IndexView.as_view(), name='index'), 
]