from random import choices

from django.shortcuts import render

from .models import Quote
from .forms import QuoteForm

POSTS_LIMIT = 10

def add (request):
    form = QuoteForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'page/form.html', context) 


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
    return render(request, 'page/quote.html', context)

def best(request):
    quotes = Quote.objects.values('content', 'source__title', 'source__author', 'likes', 'dislikes')[:POSTS_LIMIT]
    context = {'quotes': quotes}
    return render(request, 'page/best.html', context)