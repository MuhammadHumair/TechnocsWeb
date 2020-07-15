from django.shortcuts import render, redirect
from django.contrib import messages, sessions
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        data = auth.authenticate(username=uname, password=pwd)

        if data is not None:
            auth.login(request, data)
            request.session['username'] = data.username
            #messages.success(request, "Login Successfully...!!!")
            return redirect('/adminpanel/')
        else:
            messages.info(request, "Login and Password not matched...!!!")
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def logout(request):
    if 'username' in request.session:
        del request.session['username']
    auth.logout(request)
    return redirect("/")