from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Building

# Create your views here.

POSTS_PER_PAGE = 5

def home(request):
    return render(request, 'main.html')


def contact(request):
    return render(request, 'contact.html')

def cost(request):
    return render(request, 'cost.html')

def projects(request):
    buildings = Building.objects.all()
    return render(request, 'projects.html', {'buildings': buildings})

def project(request, pk):
    building = Building.objects.get(pk=pk)
    return render(request, "project.html", {'building': building})
