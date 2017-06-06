from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django import forms
from django.core.mail import send_mail
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Transaction
from .models import Category
from .models import Mail
from .models import Filter

class DateInput(forms.DateInput):
     input_type = 'date'

class NumberInput(forms.NumberInput):
     input_type = 'number'

class EmailInput(forms.EmailInput):
     input_type = 'email'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title' , 'date', 'value', 'user', 'category']
        widgets = { 'date': DateInput(), 
                    'value': NumberInput(attrs={'step': 0.01}) }

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['dateStart', 'dateEnd', 'user']
        widgets = { 'dateStart': DateInput(), 
                    'dateEnd' : DateInput() }

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['adress', 'subject', 'message']
        widgets = {'adress': EmailInput() }

def filter_transactions(request):
    if request.method == 'POST':
        formset = FilterForm(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            dateStart = data['dateStart']
            dateEnd = data['dateEnd']
            userForm = data['user']
            transactions = Transaction.objects.filter(date__gte = request.POST['dateStart'] , date__lte = request.POST['dateEnd'] , user = userForm)
            return render_to_response('polls/filter_transactions.html', {'transactions': transactions })

        
@login_required
def add_transaction(request):
    if request.method == 'POST':
        formset = TransactionForm(request.POST)
        #formset.user = request.user.id
        if formset.is_valid():
            formset.save()
            return redirect('/transactions/')
    else:
        formset = TransactionForm()
    return render_to_response('polls/add_transaction.html', {'formset' : formset})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    formset = TransactionForm(request.POST or None, instance=transaction)
    if formset.is_valid():
        formset.save()
        return redirect('/transactions/')
    return render_to_response('polls/edit_transaction.html', {'formset' : formset})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('/transactions/')
    return render_to_response('polls/delete_transaction.html', {'transaction': transaction})
    
   

def home(request):
    return render(request, 'polls/home.html')

def all_transactions(request):
    try:
        transactions = Transaction.objects.all()
        #transactions = Transaction.objects.filter(user=request.user.id)
        suma = transactions.aggregate(Sum('value')).values()[0]
        formset = FilterForm()
    except Transaction.DoesNotExist:
        raise Http404("Question does not exist")
    return render_to_response('polls/transactions.html', {'transactions': transactions, 'suma':suma, 'formset' : formset})

def all_categories(request):
    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Question does not exist")
    return render_to_response("polls/categories.html", {'categories': categories})

def all_accounts(request):    
    try:
        accounts = User.objects.all()
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render_to_response('polls/accounts.html', {'accounts': accounts})    

def detail(request, transaction_id):
    try:
        transaction = Transaction.objects.get(pk=transaction_id)
    except Transaction.DoesNotExist:
        raise Http404("Transaction does not exist")
    return render(request, 'polls/detail.html', {'transaction': transaction})

def mail(request): 
    if request.method == 'POST':
        formset = MailForm(request.POST)
        if (formset.is_valid()):
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            adress = request.POST.get('adress')
            author = 'tojestoficjalnyemail@gmail.com'
            send_mail(subject, message, author, [adress])
        return redirect('/')
    else:
        formset = MailForm()
    return render_to_response('polls/mail.html', {'formset' : formset})

# return render('polls/mail.html') 