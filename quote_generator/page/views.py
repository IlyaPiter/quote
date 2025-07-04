from random import choices
import pdb

from django.shortcuts import render

from .models import Quote
from .forms import QuoteForm

def add (request):
    form = QuoteForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'form.html', context) 


def index(request):
    weights_list = list(Quote.objects.values_list('value', flat=True))
    quote = Quote.objects.get(pk=choices(
        range (1, len(weights_list)+1), weights=weights_list)[0])
    quote.views += 1
    quote.save()
    context = {'quote': quote}   
    if request.method == 'POST':
        if request.POST.get('like'):
            quote.likes += 1
            quote.save()

        elif request.POST.get('dislike'):
            quote.dislikes += 1
            quote.save()

    return render(request, 'quote.html', context)
