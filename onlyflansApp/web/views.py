from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactFormForm
from .models import Flan, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    
    return render(
        request,
        'index.html',
        {
            'public_flans': public_flans
        })

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    
    return render(
        request,
        'welcome.html',
        {
            'private_flans': private_flans
        })

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito')
    else:
        form = ContactFormForm()

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

def registro(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenido')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

