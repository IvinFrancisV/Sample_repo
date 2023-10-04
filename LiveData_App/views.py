from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request, "sample.html")

def view_about(request):
    return render(request, "about.html")