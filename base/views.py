from django.shortcuts import render
from base.provider import Provider

def home(request):
    return render(request, 'base/home.html', {})

def imprint(request):
    return render(request, 'base/imprint.html', {'provider' : Provider,})

def privacy_policy(request):
    return render(request, 'base/privacy_policy.html', {'provider' : Provider,})