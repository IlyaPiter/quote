from random import randint

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Quote
from .forms import QuoteForm

def add (request):
    form = QuoteForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'form.html', context) 


def index(request):
    context = {
        'quote': Quote.objects.get(pk=randint(1, Quote.objects.count()))
        }
    return render(request, 'quote.html', context)
