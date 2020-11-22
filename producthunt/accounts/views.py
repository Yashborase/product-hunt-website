from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method=='post':
        if request.POST['password1']==request.POST['password2']:
            try:
                User.objects.get(username=POST['username'])
                return render(request,'accounts/signup.html',{'error':'username already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error': 'Password mismatched'})

    else:
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/logout.html')