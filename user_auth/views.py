from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from user_auth.services import UserAuthServices


def index(request):
    """
    Home page renders index template
    """
    return render(request, 'index.html')


def signup(request):
    """
    renders signup template
    handles signup POST request
    """
    if not request.method == 'POST':
        return render(request, 'signup.html')

    try:
        UserAuthServices.signup_service(request)
        return HttpResponseRedirect(reverse('home'))
    except Exception as ex:
        messages.error(request, ex)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
