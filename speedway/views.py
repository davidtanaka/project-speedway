from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def estimates(request):
    return render(request, 'estimates.html')

def contact(request):
    return render(request, 'contact.html')
