#views for the 'shopping' django app

from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Item, Store
from django.views.generic.edit import FormView

# Create your views here.
def index(request):
    items_needed = Item.objects.order_by('-itemAdded')
    current_stores = Store.objects.order_by('storeName')
    context = {'items_needed': items_needed, 'current_stores': current_stores}
    
    return render(request, 'shopping/shopping-index.html', context)

def item(request):
    if request.method == 'POST':
        #delete the item(s) selected
        delete_item_id = request.POST['item_id']
        deleting_item = Item.objects.get(pk=delete_item_id)
        
        deleting_item.delete()

        return HttpResponseRedirect('items')
    else:
        items_needed = Item.objects.order_by('-itemAdded')
        context = {'items_needed': items_needed}
        return render(request, 'shopping/shopping-items.html', context)

def additem(request):
    if request.method == 'POST':
        item = Item()
        item.itemName = request.POST['additemname']
        item.itemDescription = request.POST['additemdescription']
        item.itemQuantity = request.POST['additemquantity']
        item.itemAdded = timezone.now()
        storeID = request.POST['additemstore']
        item.itemStore = get_object_or_404(Store, pk=storeID)
        item.itemPurchased = False

        item.save(force_insert=True)

        return HttpResponseRedirect('items')
    else:
        c_stores = Store.objects.order_by('storeName')
        context = {'c_stores': c_stores}
        return render(request, 'shopping/shopping-add-item.html', context)

def itemdetail(request, pk):
    selected_item = get_object_or_404(Item, pk=pk)
    context = {'pk': pk, 'selected_item': selected_item}
    return render(request, 'shopping/shopping-detail-item.html', context)

def itemdelete(request):
    if request.method == 'POST':
        this_pk = int(request.POST['item_id'])
        this_item = get_object_or_404(Item, itemID=this_pk)

        this_item.delete()

        return HttpResponseRedirect('items')
    else:
        return HttpResponseRedirect('items')


def store(request):
    current_stores = Store.objects.order_by('storeName')
    context = {'current_stores': current_stores}
    return render(request, 'shopping/shopping-stores.html', context)

def addstore(request):
    if request.method == 'POST':
        store = Store()
        store.storeName = request.POST['addstorename']
        store.storeLocation = request.POST['addstorelocation']
        store.storeStreet = request.POST['addstorestreet']
        store.storeCity = request.POST['addstorecity']
        store.storeState = request.POST['addstorestate']
        store.storeZip = request.POST['addstorezip']
        
        store.save(force_insert=True)

        return HttpResponseRedirect('stores')
    else:
        return render(request, 'shopping/shopping-add-store.html')

def storedetail(request, pk):
    selected_store = get_object_or_404(Store, pk=pk)
    context = {'pk': pk, 'selected_store': selected_store}
    return render(request, 'shopping/shopping-detail-store.html', context)

def storedelete(request):
    if request.method == 'POST':
        store_pk = int(request.POST['store_id'])
        this_store = get_object_or_404(Store, storeID=store_pk)

        this_store.delete()

        return HttpResponseRedirect('stores')
    else:
        return HttpResponseRedirect('stores')


#moving away from class-based views for now
"""
class IndexView(generic.TemplateView):
    template_name='shopping/index.html'

class ItemView(generic.TemplateView):
    template_name='shopping/items.html'

class StoreView(generic.TemplateView):
    template_name='shopping/stores.html'

class AddStoreView(FormView):
    template_name='shopping/addstore.html'
    form_class = AddStore
    success_url = '/shopping/stores/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request):
        #some code here
        return pass
    
    def post(self, request):
        #some code here
        return pass
"""