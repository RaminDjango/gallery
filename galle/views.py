from django.shortcuts import render, redirect
from .models import InfoPictureAdd
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='logins')
def index(request):
    if 'q' in request.GET:
        q = request.GET["q"]
        date_add  = InfoPictureAdd.objects.filter(Q(title__icontains=q))
    else:
        date_add  = InfoPictureAdd.objects.all()
    return render(request, 'index.html', {'date_add': date_add})


@login_required(login_url='logins')
def about(request):
    return render(request, 'about.html')
@login_required(login_url='logins')
def delete(request, pk):
    d = InfoPictureAdd.objects.get(id=pk)
    d.delete()
    return redirect('home')

@login_required(login_url='logins')
def updates(request, pk):
    up = InfoPictureAdd.objects.get(id=pk)
    if request.method == 'POST':
       
        up.image = request.FILES.get('img')
        up.title = request.POST.get('title')
        up.description = request.POST.get('textare')
        up.save()
        return redirect('/')
    return render(request, 'form-info.html', {'up':up})

    
@login_required(login_url='logins')
def form(request):
    if request.method == 'POST':
        image2 = request.FILES.get('img')
        title = request.POST.get('title')
        descript = request.POST.get('textare')
        save_db = InfoPictureAdd.objects.create(image=image2, title=title, description=descript).save()
        return redirect('home')
    return render(request, 'form-info.html')


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('logins')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        password2= request.POST.get('passverify')
        if User.objects.filter(username = username).first():
            messages.info(request, 'Username it was taken try a new name.')
        elif User.objects.filter(email = email).first():
            messages.info(request, 'This email exist in are platform.')
        elif password != password2:
            messages.info(request, 'The password you put it not  matching with the first')
        else:
            create_user = User.objects.create_user(username=username, email=email, password=password)
            create_user.first_name = name
            create_user.last_name  = lastname
            create_user.save()
            return redirect('logins')
    
    return render(request, 'register.html')
@login_required(login_url='logins')
def lout(request):
    logout(request)
    return redirect('logins')
@login_required(login_url='logins')
def viePage(request, pk):
    v = InfoPictureAdd.objects.get(id=pk)
    return render(request, 'view.html', {'v':v})



