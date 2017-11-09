from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'webapp/home_page.html')


@login_required
def logout(request):
	print("h")
	auth.logout(request)
	return HttpResponseRedirect('/home')
