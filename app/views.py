from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Building
from django.core.paginator import Paginator

# Create your views here.

POSTS_PER_PAGE = 5

def home(request):
    return render(request, 'main.html')


def contact(request):
    return render(request, 'contact.html')

def cost(request):
    return render(request, 'cost.html')




def paginated_projects(request, page=1):
    buildings = Building.objects.all()
    paginator = Paginator(buildings, POSTS_PER_PAGE)
    page = paginator.page(page)
    return render(request, 'projects.html', {'buildings': page})

def project(request, pk):
    building = Building.objects.get(pk=pk)
    return render(request, "project.html", {'building': building})
