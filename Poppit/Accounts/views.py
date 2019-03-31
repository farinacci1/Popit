from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout as django_logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    render(request,'includes/Index.html',{'title':'Index'})
    return redirect('Poppit-Login')
def logIn(request):
    if request.method == 'POST':
        username = request.POST['Email']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password )
        if user:
            login(request, user)
            return redirect('Poppit-Home')
        else:
            return render(request,'includes/LogIn.html',{'title':'Login'})
    else:
        return render(request,'includes/LogIn.html',{'title':'Login'})
def signUp(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			#return redirect('blog/LogIn.html') #REDIRECT TO SOMEWHERE
	else:
		form = RegisterForm()

	return render(request,'includes/Register.html',{'title':'Registration' ,'form': form})

def profile(request):
    if request.user.is_authenticated:
        args = {"user" : request.user,'title':'MyPage'}
        return render(request,"includes/userHome.html",args)
    else:
        return redirect('Poppit-Login')
@login_required
def logout(request):
    django_logout(request)
    return redirect('Poppit-index')
