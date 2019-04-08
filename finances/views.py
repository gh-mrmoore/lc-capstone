#views for the 'finances' django app

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from datetime import datetime

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Banks, LCat, Line

#from .forms import LineForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'finances/finances-index.html'

class BanksView(generic.ListView):
    template_name = 'finances/finances-banks-all.html'
    context_object_name = 'all_listed_banks'

    def get_queryset(self):
        return Banks.objects.order_by('bankName')

#changing this to a function-based view - I can't get it to reverse-sort
#transactions that are associated with the account this way


def bank_detail(request, bank_id):
    get_bank = get_object_or_404(Banks, pk=bank_id)
    bank_transactions = Line.objects.filter(lineBank=get_bank).order_by('-lineDT')
    context = {'bank_id': bank_id, 'get_bank': get_bank, 'bank_transactions': bank_transactions}
    return render(request, 'finances/finances-banks-transactions.html', context)

class TransactionView(generic.ListView):
    model = Line
    context_object_name = 'transactions'
    template_name = 'finances/finances-transactions-all.html'

#switching to function-based views since I'm having issues with Class-based forms
def addline(request, bank_id):
    if request.method == 'POST':
        #get the current account from the URL string
        this_bank = get_object_or_404(Banks, pk=bank_id)

        cat_id = request.POST['category']

        this_category = get_object_or_404(LCat, pk=cat_id)
        #calculate the new current balance of the account
        this_amount = float(request.POST['amount'])
        last_balance = float(request.POST['ramount'])
        new_line_balance = last_balance + this_amount

        #add the new transaction to the database
        new_line = Line()
        #new_line.lineDT = request.POST['date']
        new_line.lineDT = datetime.now()
        new_line.lineAmount = float(request.POST['amount'])
        new_line.lineShort = request.POST['short_note']
        new_line.lineLong = request.POST['long_note']
        new_line.lineCategory = this_category
        new_line.lineBank = this_bank
        new_line.lineBalance = new_line_balance

        new_line.save(force_insert=True)

        return HttpResponseRedirect('/finances/banks')
    else:
        current_bank = get_object_or_404(Banks, pk=bank_id)    #get the account from the database
        current_categories = LCat.objects.order_by('lcatDesc')    #get all the categories in the database

        #get the most recent transaction
        bank_transactions = Line.objects.filter(lineBank=current_bank)    #get the transactions for the current account
        if bank_transactions:
            most_recent_transaction = bank_transactions.reverse()[0]    #reverse the queryset and get the first item
            most_recent_balance = most_recent_transaction.lineBalance    #get the most recent balance from the most recent transaction
        else:
            most_recent_balance = 0

        right_now = timezone.now()
        context = {'current_bank': current_bank, 
                    'current_categories': current_categories, 
                    'bank_id': bank_id, 
                    'right_now': right_now, 
                    'most_recent_balance': most_recent_balance}
        return render(request, 'finances/finances-transactions-add.html', context)

def editline(request, line_id):
    if request.method == 'POST':
        #get the current line ID from the url path
        edit_this_line = get_object_or_404(Line, pk=line_id)
        edit_this_catID = request.POST['category']
        edit_this_lcat = get_object_or_404(LCat, pk=edit_this_catID)

        edit_line = Line()
        edit_line.lineID = edit_this_line.lineID
        edit_line.lineDT = edit_this_line.lineDT
        edit_line.lineAmount = float(request.POST['new_amount'])
        edit_line.lineShort = request.POST['new_line_short']
        edit_line.lineLong = request.POST['new_line_long']
        edit_line.lineCategory = edit_this_lcat
        edit_line.lineBank = edit_this_line.lineBank
        edit_line.lineBalance = edit_this_line.lineBalance    #need a calculation here instead
        #need to handle the balance mathematics on the template side or
        #some other way since an edit too far upstream would require too
        #many downstream changes to update through the view here

        edit_line.save(force_update=True)

        return HttpResponseRedirect('/finances/banks')
    else:
        #get the current line transaction
        current_line = get_object_or_404(Line, pk=line_id)

        #get all the categories available
        edit_categories = LCat.objects.order_by('lcatDesc')

        #send information to the template and render it
        context = {'current_line': current_line,
                    'edit_categories': edit_categories}
        return render(request, 'finances/finances-transactions-edit.html', context)