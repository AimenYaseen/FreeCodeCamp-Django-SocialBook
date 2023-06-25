from django.http import HttpResponse


def index(request):
    """
    Home page
    """
    return HttpResponse('<h1>Welcome to Social Book</h1>')
