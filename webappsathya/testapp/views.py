from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        print(request.user.is_authenticated)
        return render(request,'testapp/home.html',{'users':users})
    else:
        return render(request,'testapp/login_form.html')


def login_page(request):
    username = request.POST.get('user')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        print('login successful')
        users = User.objects.all()
        return render(request,'testapp/home.html',{'users':users})
    return render(request,'testapp/login_form.html')


def register_page(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name= request.POST['Name']
            email = request.POST['Email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            role = request.POST['Role']
            print(name,email,password1)
            if password1==password2:
                if User.objects.filter(username=name).exists():
                    print('useralready exist')
                    
                    return render(request,'testapp/register.html',{'name':'user already exist'})
                elif User.objects.filter(email=email).exists():
                    print('email exist')
                    return render(request,'testapp/register.html',{'name':'email already exist'})
                else:
                    if role_1=='admin':
                        user = User.objects.create_superuser(username=name,password=password1,email=email)
                        user.save()
                        print('superuser created')
                        return redirect('/')
                    else:
                        user = User.objects.create_user(username=name,password=password1,email=email)
                        user.save()
                        print('user created')
                        return redirect('/')
            else :
                print('password is incorrect')
                return render(request,'testapp/register.html',{'name':'password didnot match'})
        
        else:
            return render(request,'testapp/register.html')
    else:
        return render(request,'testapp/login_form.html')


def home_page_return(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request,'testapp/home.html',{'users':users})
    else:
        return render(request,'testapp/login_form.html')

def info_page(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request,'testapp/info.html')
    else:
        return render(request,'testapp/login_form.html')
def logout_page(request):
    logout(request)
    return redirect('/login')
