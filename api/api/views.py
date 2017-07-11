from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
	    return render(request, 'dashboard.html')