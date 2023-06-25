from django.shortcuts import render


def index(request):
    """
    Home page renders index template
    """
    return render(request, 'index.html')
