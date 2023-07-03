from django.shortcuts import render


def index(request):
    """
    Home page renders index template
    """
    return render(request, 'index.html')


def signup(request):
    """
    renders signup template
    """
    if request.method == 'POST':
        pass
    else:
        return render(request, 'signup.html')
