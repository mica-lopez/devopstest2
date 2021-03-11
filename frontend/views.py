from django.shortcuts import render
from frontend.models import Person

# Create your views here.

def index(request):
    return render(request, 'index.html', {'persons': Person.objects.all()})
