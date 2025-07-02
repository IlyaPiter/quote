# from django.shortcuts import  render
from django.http import HttpResponse

text = '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.'''

def index(request):
#    template = 'blog/index.html'
#    context = {'post_list': posts}
 #   return render(request, template, context)
    return HttpResponse (text)

