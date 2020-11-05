from django.shortcuts import render,redirect
from django.contrbb.auth import login, authenticate, logout
from authentication.forms import RegistrationForm

# Create your views here.
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            profile = authenticate(email=email, password=pass1)
            login(request,account)
            return redirect ('home')