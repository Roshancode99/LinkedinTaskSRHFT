from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'pagelayout.html')  
        else:
            return HttpResponse("Invalid credentials! Please try again.")
    return render(request, 'login.html')  

def index(request):
    return render(request , 'index.html')


def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists! Please choose another username.")

        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
        return render(request, 'index.html')
    return render(request, 'signup.html')