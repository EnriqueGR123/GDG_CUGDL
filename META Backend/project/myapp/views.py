from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu(request, dish):
    items = {
        'pasta':'pasta',
        'pastel':'pastel',
        'tacos':'tacos'
    }
    description = items[dish]
    return HttpResponse(f'<h2>Dish</h2> {dish} description {description} ')