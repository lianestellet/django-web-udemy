from django.shortcuts import render
from .models import List

def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', { 'all_items': all_items })

def about(request):
    context = { 'first_name': 'John', 'last_name': 'Snow' }
    return render(request, 'about.html', context)