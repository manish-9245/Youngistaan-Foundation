from django.shortcuts import render,redirect,HttpResponseRedirect
from . forms import RegisterVolunteerForm,CreateUserForm
from django.contrib.auth.models import User,Group
from .models import Volunteer
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):

    form = CreateUserForm()
    form_2 = RegisterVolunteerForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        form_2 = RegisterVolunteerForm(request.POST)
        if form.is_valid() and form_2.is_valid():
            user = form.save()
            group = Group.objects.get(name='Volunteer')
            user.groups.add(group)
            form_2.save()
            #volunteer = Volunteer.objects.create(user=user,name =str(user.first_name +" " +user.last_name))
            return redirect('users:login')

    context = {'form':form,'form_2':form_2}
    return render(request,"users/register.html",context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username =username, password=password)

        if user is not None:
            login(request,user)
            if(user.groups.all()[0].name == 'Volunteer'):
                return redirect("users:profile")

        else:
            return redirect("users:login")


    return render(request,"users/login.html")

def logoutUser(request):
    logout(request)
    return redirect("users:login")

def profile(request):
    user = request.user
    print(user)
    volunteer = Volunteer.objects.get(user=user)

    return render(request,'users/profile.html',{'volunteer':volunteer})