from django.shortcuts import render
from LiveData_App.models import *

# Create your views here.
def sample(request):
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render(request, "sample.html", context)


def view_about(request):
    return render(request, "about.html")