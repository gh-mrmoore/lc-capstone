#urls for the 'shopping' django app

from django.urls import path
from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'), 
    path('items', views.item, name='items'), 
    path('additem', views.additem, name='additem'), 
    path('items/<int:pk>', views.itemdetail, name='itemdetail'), 
    path('item_delete', views.itemdelete, name='itemdelete'), 
    path('stores', views.store, name='stores'), 
    path('addstore', views.addstore, name='addstore'), 
    path('stores/<int:pk>', views.storedetail, name='storedetail'), 
    path('store_delete', views.storedelete, name='storedelete'), 
    #path('', views.IndexView.as_view(), name='index'), 
    #path('items', views.ItemView.as_view(), name='items'), 
    #path('stores', views.StoreView.as_view(), name='stores'), 
    #path('addstore', views.AddStoreView.as_view(), name='addstore'), 
]